# Git Workflow Guidelines

## Atomic Commits

### Principles

1. **One logical change per commit**: Each commit should represent a single, complete change that makes sense on its own.
2. **Keep commits small**: Prefer multiple small commits over one large commit.
3. **Buildable commits**: Each commit should leave the codebase in a buildable state.

### Size Guidelines

- **Maximum lines per commit**: 50 lines of changes
- **Maximum files per commit**: 5 files
- **Exception**: When files are tightly coupled (e.g., interface and implementation), they can be committed together even if they exceed these limits.

### When to Split Commits

Split a commit if:
- It contains unrelated changes (e.g., bug fix + new feature)
- It modifies more than 5 files
- It contains more than 50 lines of changes
- It mixes different types of changes (e.g., refactoring + feature addition)

## Dependency Analysis

### Identifying Related Files

Files should be grouped together if they:
- Import or depend on each other
- Are part of the same feature/module
- Are updated together to maintain consistency
- Share the same change type (feat, fix, refactor, etc.)

### Examples

**Good grouping:**
- API endpoint definition + frontend component that uses it
- Database migration + model changes
- Interface definition + implementations
- Test file + source file being tested

**Bad grouping:**
- Unrelated bug fixes
- Different features
- Style changes mixed with logic changes

## Testing Before Commit

### Test Execution

Before committing, run the project's test suite:
- `npm test` for Node.js projects
- `pytest` or `python -m pytest` for Python projects
- `./test.sh` for custom test scripts

### Test Failures

If tests fail:
- Do not commit the changes
- Fix the issues first
- Re-run tests before committing

### Skipping Tests

Tests can be skipped only when:
- Tests are not available for the project
- Changes are documentation-only
- Changes are configuration-only (with caution)

## Commit Message Quality

### Good Commit Messages

- Clear and descriptive
- Use imperative mood ("add feature" not "added feature")
- Include context when necessary
- Reference issues when applicable

### Bad Commit Messages

- Vague ("fix stuff", "update")
- Past tense ("fixed bug", "updated file")
- Too long or too short
- Missing context

## Pre-commit Checklist

Before committing, verify:
1. [ ] All related files are included
2. [ ] Unrelated changes are separated
3. [ ] Tests pass (if applicable)
4. [ ] Commit message follows Conventional Commits
5. [ ] Code builds successfully
6. [ ] No debug code or temporary files included

## Post-commit Review

After committing:
1. Review the commit with `git show`
2. Verify all intended changes are included
3. Check that commit message accurately describes changes
4. Ensure no sensitive information was committed
