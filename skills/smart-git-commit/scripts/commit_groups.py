#!/usr/bin/env python3
"""
Execute git commits for grouped changes.

This script takes commit groups (from analyze_changes.py) and
executes git add and git commit for each group sequentially.
"""

import subprocess
import json
import sys
from typing import List, Dict


def run_git_command(cmd: List[str], check: bool = True) -> tuple[str, int]:
    """Execute a git command and return output and exit code."""
    try:
        result = subprocess.run(
            ["git"] + cmd,
            capture_output=True,
            text=True,
            check=check
        )
        return result.stdout.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        return e.stderr.strip(), e.returncode


def stage_files(files: List[str]) -> bool:
    """Stage files for commit."""
    if not files:
        return False
    
    output, code = run_git_command(["add"] + files, check=False)
    if code != 0:
        print(f"Error staging files: {output}", file=sys.stderr)
        return False
    return True


def commit_changes(header: str, body: str = "") -> bool:
    """Commit staged changes with message."""
    message = header
    if body:
        message = f"{header}\n\n{body}"
    
    output, code = run_git_command(
        ["commit", "-m", message],
        check=False
    )
    if code != 0:
        print(f"Error committing: {output}", file=sys.stderr)
        return False
    return True


def push_changes(branch: str = None) -> bool:
    """Push commits to remote."""
    if branch is None:
        # Get current branch
        output, code = run_git_command(["rev-parse", "--abbrev-ref", "HEAD"], check=False)
        if code != 0:
            print(f"Error getting current branch: {output}", file=sys.stderr)
            return False
        branch = output.strip()
    
    output, code = run_git_command(["push", "origin", branch], check=False)
    if code != 0:
        print(f"Error pushing: {output}", file=sys.stderr)
        return False
    return True


def run_tests() -> bool:
    """Run project tests if test script exists."""
    # Check for common test commands
    test_commands = [
        ["npm", "test"],
        ["python", "-m", "pytest"],
        ["pytest"],
        ["python", "-m", "unittest", "discover"],
        ["./test.sh"],
    ]
    
    for cmd in test_commands:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            if result.returncode == 0:
                print(f"Tests passed with: {' '.join(cmd)}")
                return True
            else:
                print(f"Tests failed with: {' '.join(cmd)}", file=sys.stderr)
                print(result.stderr, file=sys.stderr)
                return False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    # No test command found, assume tests pass
    print("No test command found, skipping tests")
    return True


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: commit_groups.py <commits_json> [--skip-tests] [--no-push]", file=sys.stderr)
        sys.exit(1)
    
    skip_tests = "--skip-tests" in sys.argv
    no_push = "--no-push" in sys.argv
    
    # Read commit groups from JSON
    try:
        with open(sys.argv[1], 'r') as f:
            commits = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)
    
    if not commits:
        print("No commits to process.")
        return
    
    # Show commit plan
    print("Commit Plan:")
    print("=" * 60)
    for i, commit in enumerate(commits, 1):
        print(f"\n{i}. {commit['header']}")
        print(f"   Files: {len(commit['files'])}")
        for f in commit['files'][:3]:
            print(f"     - {f}")
        if len(commit['files']) > 3:
            print(f"     ... and {len(commit['files']) - 3} more")
    print("\n" + "=" * 60)
    
    # Ask for confirmation
    response = input("\nProceed with commits? (yes/no): ").strip().lower()
    if response not in ["yes", "y"]:
        print("Aborted.")
        return
    
    # Execute commits
    successful_commits = []
    failed_commits = []
    
    for i, commit in enumerate(commits, 1):
        print(f"\n[{i}/{len(commits)}] Committing: {commit['header']}")
        
        # Stage files
        if not stage_files(commit['files']):
            print(f"Failed to stage files for commit {i}")
            failed_commits.append(commit)
            continue
        
        # Run tests if not skipped
        if not skip_tests:
            print("Running tests...")
            if not run_tests():
                print("Tests failed. Aborting commit.", file=sys.stderr)
                # Unstage files
                run_git_command(["reset"], check=False)
                failed_commits.append(commit)
                break
        
        # Commit
        if not commit_changes(commit['header'], commit.get('body', '')):
            print(f"Failed to commit {i}")
            failed_commits.append(commit)
            continue
        
        print(f"✓ Committed: {commit['header']}")
        successful_commits.append(commit)
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Successful: {len(successful_commits)}")
    print(f"  Failed: {len(failed_commits)}")
    
    if failed_commits:
        print("\nFailed commits:")
        for commit in failed_commits:
            print(f"  - {commit['header']}")
    
    # Check for remaining uncommitted changes
    output, code = run_git_command(["status", "--porcelain"], check=False)
    if code == 0 and output.strip():
        remaining = [line for line in output.strip().split("\n") if line.strip()]
        if remaining:
            print("\n⚠ Warning: There are remaining uncommitted changes:")
            for line in remaining[:10]:
                print(f"  {line}")
            if len(remaining) > 10:
                print(f"  ... and {len(remaining) - 10} more")
            print("\nYou may want to run analyze_changes.py again to commit remaining changes.")
    
    # Push automatically by default (unless --no-push is specified)
    if successful_commits and not no_push:
        # Check if there are commits to push
        branch_output, branch_code = run_git_command(["rev-parse", "--abbrev-ref", "HEAD"], check=False)
        if branch_code == 0:
            branch = branch_output.strip()
            log_output, log_code = run_git_command(["log", f"origin/{branch}..HEAD", "--oneline"], check=False)
            if log_code == 0 and log_output.strip():
                commits_to_push = len(log_output.strip().split("\n"))
                print(f"\n{commits_to_push} commit(s) ready to push.")
                
                # Auto-push by default (unless explicitly disabled with --no-push)
                print("Pushing to remote...")
                if push_changes():
                    print("✓ Successfully pushed to remote")
                else:
                    print("✗ Failed to push to remote", file=sys.stderr)
                    sys.exit(1)
            else:
                print("\nNo commits to push.")
        else:
            print("\nCould not determine current branch. Skipping push check.")


if __name__ == "__main__":
    main()
