#!/usr/bin/env python3
"""
Analyze git changes and group them logically for atomic commits.

This script analyzes unstaged changes in the working directory,
groups related changes together, and suggests commit messages
following Conventional Commits specification.
"""

import subprocess
import re
import json
from pathlib import Path
from typing import List, Dict, Set, Tuple
from collections import defaultdict
import sys


def run_git_command(cmd: List[str], check: bool = True):
    """Execute a git command and return output (and exit code if check=False)."""
    try:
        result = subprocess.run(
            ["git"] + cmd,
            capture_output=True,
            text=True,
            check=check
        )
        if check:
            return result.stdout.strip()
        return result.stdout.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        if check:
            print(f"Error running git command: {' '.join(cmd)}", file=sys.stderr)
            print(f"Error: {e.stderr}", file=sys.stderr)
            sys.exit(1)
        return e.stderr.strip(), e.returncode


def get_unstaged_files() -> List[str]:
    """Get list of unstaged modified files and untracked files."""
    files = []
    
    # Get modified files
    output = run_git_command(["diff", "--name-only"])
    if output:
        files.extend(output.split("\n"))
    
    # Get untracked files
    output = run_git_command(["ls-files", "--others", "--exclude-standard"])
    if output:
        files.extend(output.split("\n"))
    
    # Remove empty strings
    files = [f for f in files if f.strip()]
    
    return files


def get_file_diff(filepath: str) -> str:
    """Get the diff for a specific file."""
    # Check if file is tracked
    output, code = run_git_command(["ls-files", "--error-unmatch", filepath], check=False)
    if code == 0:
        # File is tracked, get diff
        return run_git_command(["diff", filepath])
    else:
        # File is untracked, return empty diff (will be treated as new file)
        return ""


def analyze_file_type(filepath: str) -> str:
    """Determine the type of file based on extension."""
    ext = Path(filepath).suffix.lower()
    type_map = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".jsx": "react",
        ".tsx": "react",
        ".php": "php",
        ".java": "java",
        ".go": "go",
        ".rs": "rust",
        ".css": "css",
        ".scss": "css",
        ".html": "html",
        ".md": "documentation",
        ".json": "config",
        ".yml": "config",
        ".yaml": "config",
        ".xml": "config",
        ".sql": "database",
        ".sh": "script",
        ".txt": "text",
    }
    return type_map.get(ext, "other")


def extract_imports_and_dependencies(diff_content: str, filepath: str) -> Set[str]:
    """Extract imports and dependencies from diff to identify related files."""
    dependencies = set()
    
    # Extract import statements
    import_patterns = [
        r'^\+import\s+["\']([^"\']+)["\']',  # Python/JS imports
        r'^\+from\s+([^\s]+)\s+import',  # Python from imports
        r'^\+require\(["\']([^"\']+)["\']\)',  # Node.js require
        r'^\+#include\s+["<]([^">]+)[">]',  # C/C++ includes
        r'^\+use\s+([^\s;]+)',  # PHP use statements
    ]
    
    for pattern in import_patterns:
        matches = re.findall(pattern, diff_content, re.MULTILINE)
        for match in matches:
            # Normalize path (remove relative parts)
            normalized = match.replace("../", "").replace("./", "")
            dependencies.add(normalized)
    
    return dependencies


def classify_change_type(diff_content: str, filepath: str) -> str:
    """Classify the type of change based on diff content."""
    # If diff is empty, it's likely a new untracked file
    if not diff_content:
        # Classify based on file extension/path
        if filepath.endswith((".md", ".txt", ".rst")) or "doc" in filepath.lower():
            return "docs"
        if "test" in filepath.lower() or "spec" in filepath.lower():
            return "test"
        if any(keyword in filepath.lower() for keyword in ["config", "setting", "env"]):
            return "config"
        return "feat"  # New files are typically features
    
    diff_lower = diff_content.lower()
    
    # Feature additions
    if any(keyword in diff_lower for keyword in ["add", "new", "create", "implement", "feat"]):
        if "fix" in diff_lower or "bug" in diff_lower or "error" in diff_lower:
            return "fix"
        return "feat"
    
    # Bug fixes
    if any(keyword in diff_lower for keyword in ["fix", "bug", "error", "issue", "correct"]):
        return "fix"
    
    # Refactoring
    if any(keyword in diff_lower for keyword in ["refactor", "restructure", "reorganize", "cleanup"]):
        return "refactor"
    
    # Style changes
    if any(keyword in diff_lower for keyword in ["style", "format", "indent", "whitespace"]):
        return "style"
    
    # Documentation
    if filepath.endswith((".md", ".txt", ".rst")) or "doc" in filepath.lower():
        return "docs"
    
    # Performance
    if any(keyword in diff_lower for keyword in ["performance", "optimize", "speed", "cache"]):
        return "perf"
    
    # Tests
    if "test" in filepath.lower() or "spec" in filepath.lower():
        return "test"
    
    # Configuration
    if any(keyword in diff_lower for keyword in ["config", "setting", "env"]):
        return "config"
    
    # Default to refactor for unclear cases
    return "refactor"


def extract_scope(filepath: str) -> str:
    """Extract scope from filepath."""
    parts = Path(filepath).parts
    
    # Common scope patterns
    if len(parts) > 1:
        # Use parent directory as scope
        scope = parts[0] if parts[0] not in [".", ".."] else (parts[1] if len(parts) > 1 else "global")
        
        # Normalize common scopes
        scope_map = {
            "src": "core",
            "lib": "core",
            "app": "app",
            "admin": "admin",
            "theme": "theme",
            "adm": "admin",
        }
        return scope_map.get(scope.lower(), scope.lower())
    
    return "global"


def count_changes(diff_content: str) -> Tuple[int, int]:
    """Count added and removed lines."""
    added = len(re.findall(r'^\+', diff_content, re.MULTILINE))
    removed = len(re.findall(r'^-', diff_content, re.MULTILINE))
    return added, removed


def group_related_files(files: List[str], diffs: Dict[str, str]) -> List[List[str]]:
    """Group files that are logically related."""
    # Build dependency graph
    file_deps = {}
    for filepath in files:
        diff = diffs.get(filepath, "")
        deps = extract_imports_and_dependencies(diff, filepath)
        file_deps[filepath] = deps
    
    # Group by change type and scope
    groups = defaultdict(list)
    for filepath in files:
        diff = diffs.get(filepath, "")
        change_type = classify_change_type(diff, filepath)
        scope = extract_scope(filepath)
        key = (change_type, scope)
        groups[key].append(filepath)
    
    # Further refine groups by checking dependencies
    refined_groups = []
    processed = set()
    
    for (change_type, scope), group_files in groups.items():
        if not group_files:
            continue
        
        # Check if files in this group have dependencies on each other
        current_group = []
        for filepath in group_files:
            if filepath in processed:
                continue
            
            # Check if this file depends on or is depended upon by other files in the group
            file_deps_set = file_deps.get(filepath, set())
            related = [f for f in group_files if f != filepath and 
                      (any(dep in f for dep in file_deps_set) or 
                       any(dep in filepath for dep in file_deps.get(f, set())))]
            
            if related or not current_group:
                current_group.append(filepath)
                processed.add(filepath)
            else:
                # Start a new group if not related
                if current_group:
                    refined_groups.append(current_group)
                current_group = [filepath]
                processed.add(filepath)
        
        if current_group:
            refined_groups.append(current_group)
    
    return refined_groups


def generate_commit_message(files: List[str], diffs: Dict[str, str]) -> Tuple[str, str]:
    """Generate commit message following Conventional Commits."""
    if not files:
        return "", ""
    
    # Determine change type and scope from first file
    first_file = files[0]
    diff = diffs.get(first_file, "")
    change_type = classify_change_type(diff, first_file)
    scope = extract_scope(first_file)
    
    # If multiple scopes, use a general one
    scopes = {extract_scope(f) for f in files}
    if len(scopes) > 1:
        scope = "global"
    
    # Generate subject from file changes
    file_names = [Path(f).stem for f in files]
    
    # Check if files are new (untracked)
    new_files = []
    for f in files:
        output, code = run_git_command(["ls-files", "--error-unmatch", f], check=False)
        if code != 0:
            new_files.append(f)
    
    if len(files) == 1:
        if new_files:
            subject = f"add {file_names[0]}"
        else:
            subject = f"update {file_names[0]}"
    elif len(files) <= 3:
        if len(new_files) == len(files):
            subject = f"add {', '.join(file_names)}"
        elif new_files:
            subject = f"add {len(new_files)} new files and update {len(files) - len(new_files)} files"
        else:
            subject = f"update {', '.join(file_names)}"
    else:
        if new_files:
            subject = f"add {len(new_files)} new files and update {len(files) - len(new_files)} files"
        else:
            subject = f"update {len(files)} files"
    
    # Try to extract more meaningful subject from diff
    diff_lower = diff.lower()
    if not diff_lower:  # New file
        subject = f"add {file_names[0] if len(files) == 1 else 'files'}"
    elif "add" in diff_lower or "new" in diff_lower:
        subject = f"add {file_names[0] if len(files) == 1 else 'features'}"
    elif "fix" in diff_lower or "bug" in diff_lower:
        subject = f"fix issue in {file_names[0] if len(files) == 1 else 'components'}"
    elif "refactor" in diff_lower:
        subject = f"refactor {file_names[0] if len(files) == 1 else 'code'}"
    
    # Build commit message
    type_scope = f"{change_type}({scope})" if scope != "global" else change_type
    header = f"{type_scope}: {subject}"
    
    # Build body
    body_lines = []
    if len(files) > 1:
        body_lines.append(f"Modified {len(files)} files:")
        for f in files[:5]:  # Limit to 5 files in body
            body_lines.append(f"  - {f}")
        if len(files) > 5:
            body_lines.append(f"  ... and {len(files) - 5} more")
    
    body = "\n".join(body_lines)
    
    return header, body


def check_commit_size(files: List[str], diffs: Dict[str, str]) -> bool:
    """Check if commit group is too large and should be split."""
    total_lines = 0
    for filepath in files:
        diff = diffs.get(filepath, "")
        added, removed = count_changes(diff)
        total_lines += added + removed
    
    # Atomic commit enforcement: max 50 lines or 5 files
    if total_lines > 50 or len(files) > 5:
        return False
    return True


def main():
    """Main analysis function."""
    # Get unstaged files
    files = get_unstaged_files()
    
    if not files:
        print("No unstaged changes found.")
        return
    
    # Get diffs for all files
    diffs = {}
    for filepath in files:
        diffs[filepath] = get_file_diff(filepath)
    
    # Group related files
    groups = group_related_files(files, diffs)
    
    # Generate commit messages for each group
    commits = []
    for group in groups:
        if not check_commit_size(group, diffs):
            print(f"Warning: Group with {len(group)} files and large diff may need splitting", file=sys.stderr)
        
        header, body = generate_commit_message(group, diffs)
        commits.append({
            "files": group,
            "header": header,
            "body": body,
            "type": classify_change_type(diffs.get(group[0], ""), group[0]),
            "scope": extract_scope(group[0])
        })
    
    # Output as JSON
    print(json.dumps(commits, indent=2))


if __name__ == "__main__":
    main()
