---
name: smart-git-commit
description: Analyzes unstaged git changes, groups related modifications logically, and commits them following Conventional Commits specification with dependency-aware grouping, test integration, and atomic commit enforcement. This skill should be used when users want to commit and push multiple related changes together, when they need intelligent grouping of file changes, or when they want to ensure commits follow project conventions.
---

# Smart Git Commit

## Overview

To analyze unstaged changes in the working directory, group them logically based on dependencies and change types, and commit them following Conventional Commits specification. The skill ensures atomic commits, runs tests before committing, and maintains consistency with project commit history patterns.

## Workflow

### Step 1: Analyze Changes

To analyze unstaged changes, run the analysis script:

```bash
python3 scripts/analyze_changes.py > commits.json
```

The script performs:
- Diff analysis of all unstaged files
- Change type classification (feat, fix, refactor, style, docs, etc.)
- Dependency extraction from imports and function calls
- Logical grouping of related files
- Commit message generation following Conventional Commits
- Atomic commit size validation (max 50 lines, 5 files per commit)

The output is a JSON array of commit groups, each containing:
- `files`: List of file paths to commit together
- `header`: Commit message header (type(scope): subject)
- `body`: Optional commit message body
- `type`: Change type (feat, fix, refactor, etc.)
- `scope`: Scope identifier (admin, theme, core, etc.)

### Step 2: Review Commit History

To learn project-specific commit patterns, examine recent commit history:

```bash
git log -n 20 --oneline
git log -n 20 --format="%s%n%b" > recent_commits.txt
```

Review the commit messages to understand:
- Project-specific terminology and tone
- Common scope names used in the project
- Typical commit message structure
- Feature naming conventions

Adjust generated commit messages to match the project's style while maintaining Conventional Commits format.

### Step 3: Execute Commits

To commit the grouped changes:

```bash
python3 scripts/commit_groups.py commits.json
```

Options:
- `--skip-tests`: Skip test execution before committing
- `--no-push`: Skip pushing to remote (by default, commits are automatically pushed)

The script:
1. Displays commit plan for review
2. Prompts for confirmation
3. For each group:
   - Stages files with `git add`
   - Runs tests (unless skipped)
   - Commits with generated message
4. Checks for remaining uncommitted changes and warns if any exist
5. Automatically pushes to remote after all commits succeed (unless `--no-push` is specified)

### Step 4: Dependency-Aware Grouping

When analyzing changes, identify related files through:

- **Import analysis**: Files that import each other should be grouped together
- **Function call tracking**: Files that call functions from each other
- **Scope matching**: Files in the same directory/module with same change type
- **Semantic similarity**: Files modified for the same feature or fix

Example: If `admin/user_list.php` imports functions from `admin/utils.php` and both are modified, they should be in the same commit group.

### Step 5: Atomic Commit Enforcement

To ensure commits are atomic and manageable:

- **Size limits**: Split commits if they exceed 50 lines or 5 files
- **Change type consistency**: Don't mix feat, fix, and refactor in one commit
- **Dependency completeness**: Ensure all related files are included to prevent broken builds

When a group exceeds limits, split it by:
1. Separating by change type
2. Separating by scope/module
3. Separating by feature boundaries

### Step 6: Test Integration

Before each commit, run project tests:

- Detect test command: `npm test`, `pytest`, `python -m unittest`, `./test.sh`
- Execute tests with timeout (5 minutes)
- Abort commit if tests fail
- Skip tests only for documentation-only or config-only changes

If tests fail, unstage files and report the failure before proceeding to next commit.

## Resources

### scripts/

**analyze_changes.py**: Analyzes unstaged git changes, groups related files, and generates commit messages. Reads git diff output, classifies change types, extracts dependencies, and outputs JSON commit groups.

**commit_groups.py**: Executes git commits for grouped changes. Takes JSON commit groups, stages files, runs tests, commits with messages, and optionally pushes to remote.

### references/

**conventional_commits.md**: Complete specification for Conventional Commits format, including type definitions, scope usage, subject guidelines, and examples. Reference when generating commit messages.

**git_workflow.md**: Guidelines for atomic commits, dependency analysis, testing procedures, and commit message quality. Use for understanding best practices when grouping and committing changes.

## Usage Examples

### Example 1: Multiple Related Files

When user has modified:
- `admin/user_list.php` (adds new function)
- `admin/user_utils.php` (adds helper function used by user_list.php)
- `theme/basic/skin/admin/user_list.skin.php` (updates UI)

The skill groups `user_list.php` and `user_utils.php` together (dependency), and `user_list.skin.php` separately (different scope), creating two commits:
1. `feat(admin): add user list functionality`
2. `feat(theme): update user list UI`

### Example 2: Large Change Set

When user has 10 files modified with 200+ lines of changes:
- Analyze and split into logical groups
- Create multiple atomic commits (max 5 files, 50 lines each)
- Maintain dependency relationships within groups

### Example 3: Mixed Change Types

When user has:
- Bug fix in `api/auth.php`
- New feature in `admin/dashboard.php`
- Style changes in `css/main.css`

The skill creates three separate commits:
1. `fix(api): resolve authentication issue`
2. `feat(admin): add dashboard feature`
3. `style(css): update main stylesheet`

## Best Practices

1. **Always review commit plan**: Show the user the planned commits before executing
2. **Respect project conventions**: Learn from existing commit history and match the style
3. **Preserve build integrity**: Never commit partial changes that break the build
4. **Test before commit**: Run tests for each commit group unless explicitly skipped
5. **Atomic commits**: Split large changes into smaller, logical units
6. **Clear messages**: Generate descriptive commit messages that explain what and why
