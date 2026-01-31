# Conventional Commits Specification

## Overview

The Conventional Commits specification is a lightweight convention on top of commit messages. It provides an easy set of rules for creating an explicit commit history, which makes it easier to write automated tools on top of.

## Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

## Type

The type must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

## Scope

The scope should be the name of the package affected (as perceived by the person reading the changelog generated from commit messages).

Examples:
- `feat(parser): add ability to parse arrays`
- `fix(admin): resolve login issue`
- `refactor(theme): improve component structure`

## Subject

The subject contains a succinct description of the change:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize the first letter
- no dot (.) at the end

## Body

The body should include the motivation for the change and contrast this with previous behavior.

- use the imperative, present tense
- include the reason for the change
- wrap at 72 characters

## Footer

The footer should contain any information about Breaking Changes and is also the place to reference GitHub issues that this commit closes.

Example:
```
BREAKING CHANGE: API now requires authentication token

Closes #123
```

## Examples

```
feat(auth): add OAuth2 support

Implement OAuth2 authentication flow to support third-party login providers.

Closes #45
```

```
fix(api): resolve null pointer exception

Fixed null pointer exception that occurred when processing empty request bodies.

Fixes #123
```

```
refactor(utils): simplify date formatting logic

Extracted date formatting into separate utility function to improve code reusability.
```

```
docs(readme): update installation instructions

Added missing dependency installation steps for Node.js 18+.
```
