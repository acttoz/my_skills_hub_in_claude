---
name: debug-on-container
description: Automatically corrects debug log paths in PHP code to work seamlessly between Docker containers and host systems. This skill should be used when generating debug logging code in PHP files that need to run in Docker container environments, or when fixing existing debug log paths that use host-specific absolute paths.
---

# Debug On Container

## Overview

This skill ensures that debug logging code in PHP files works correctly in Docker container environments by automatically using container-aware paths. When generating debug log code, it enforces a pattern that uses container-mounted volume paths instead of host-specific absolute paths, preventing log files from being lost between the host and container.

## Core Rules

### Path Mapping Principle
Prefer to detect the container-side project root from `compose.yml` volume mappings (e.g. `- ./:/var/www/html`), and use that path (here `/var/www/html`) as the base; only fall back to a hard-coded default if no compose information is available.

### Absolute Path Prohibition
Never write host-specific absolute paths like `/home/ubuntu/...` directly in code.

### Dynamic Path Generation
All log paths must be written relative to the container's mounted volume, using `__DIR__` or project root constants to determine paths dynamically.

### Permission Guarantee
Before writing log files, always check if the directory exists (`is_dir`) and create it with 0777 permissions if needed to prevent permission errors.

---

## Lessons from a Real Debugging Incident

This skill is informed by an actual debugging session where logs **appeared not to be written for ~30 minutes**, even though `file_put_contents` itself was fine. The main causes were:

- Mixing **container web requests** (via Docker) with **WSL CLI runs** (`php foo.php`) that used different DB config and could die early in `_common.php`.
- Using path expressions like `__DIR__ . '/../.cursor'` / project-root constants without first aligning them with the **actual container volume mapping**, so the file opened in the editor was not always the same file the container wrote to.
- Placing logs only at “middle” points (after `_common.php`, after auth checks), so early exits meant those log lines never executed.

Key takeaways incorporated into this skill:

1. **Use container-absolute paths derived from compose.yml**
   - For a mapping like `- ./:/var/www/html`, treat `/var/www/html` as the canonical container project root.
   - Then always log to `/var/www/html/.cursor/debug.log`, which corresponds to `<hostProjectRoot>/.cursor/debug.log` on the host.

2. **Start with a very early, plain-text “top” log**
   - At the very top of the PHP file, before includes:
     ```php
     @file_put_contents('/var/www/html/.cursor/debug.log', "config_memo_update.php:top\n", FILE_APPEND);
     ```
   - This answers “Is this file actually executing in this environment?” before adding structured JSON logs.

3. **Define `$logFile` once and reuse it everywhere**
   - Set `$debugDir` / `$logFile` at the top (after confirming the directory exists) and reuse the same `$logFile` for all later logs.
   - This produces a single, ordered timeline: `top`, `after_require`, `before_auth_check`, `before_query`, `after_query`, `success` / `query_failed`, `before_exit`, etc.

4. **Always record DB error messages**
   - Include `mysqli_error()` / `mysql_error()` values in JSON logs around DB calls so schema or permission issues (e.g. `Unknown column 'cf1'`) are immediately visible.

These lessons shape the implementation pattern below.

## Implementation Pattern

When generating debug logging code, always follow this structure (with the container root first derived from `compose.yml` when available), and then reuse the same `$logFile` for all subsequent logs in that file:

```php
// 0. Container root detection (conceptual, driven by compose.yml)
// - Read docker-compose / compose.yml
// - Find a volume mapping like "./:/var/www/html" (or similar)
// - Treat the right-hand side (e.g. "/var/www/html") as $containerRoot
//   If compose.yml is not available, you MAY fall back to a known project root
//   constant (e.g. G5_PATH) or a sane default like "/var/www/html".

// 1. Path definition: Specify .cursor folder within the shared volume
// Example using container root discovered from compose.yml:
//   $containerRoot = '/var/www/html'; // derived from "./:/var/www/html" mapping
//   $debugDir = $containerRoot . '/.cursor';
// Or using a project root constant when available:
//   $debugDir = G5_PATH . '/.cursor';
$debugDir = '/var/www/html/.cursor'; // default example; prefer compose.yml-derived value
$logFile = $debugDir . '/debug.log';

// 2. Environment preparation: Create directory if missing (prevents Permission Error)
if (!is_dir($debugDir)) {
    @mkdir($debugDir, 0777, true);
    @chmod($debugDir, 0777); 
}

// 3. Logging execution: Maintain JSON format and apply exclusive lock (LOCK_EX)
$logData = [
    'location' => '{FILE_NAME}:{LINE}',
    'message' => '{MESSAGE}',
    'data' => '{DATA_ARRAY}',
    'timestamp' => time() * 1000,
    'sessionId' => 'debug-session'
];
@file_put_contents($logFile, json_encode($logData) . "\n", FILE_APPEND | LOCK_EX);
```

In addition to the structured JSON logs above, it is often useful to add a one-line “top-of-file” text log right after `$logFile` is defined:

```php
@file_put_contents($logFile, "config_memo_update.php:top\n", FILE_APPEND | LOCK_EX);
```

This guarantees that you can quickly confirm:
- The file is actually executed (both for GET and AJAX POST).
- The container is writing to the same `.cursor/debug.log` that you are inspecting on the host.

## Alternative Path Patterns

If the project uses a different container path structure, adapt the base path accordingly:

- **Standard Docker Compose**: `/var/www/html/.cursor/debug.log`
- **Using __DIR__**: `__DIR__ . '/../.cursor/debug.log'` (if file is in subdirectory)
- **Custom mount point**: Adjust `/var/www/html` to match your `compose.yml` volume mount

## Constraints

1. **Default Behavior**: When a user requests "디버그 로그 남겨줘" (add debug log) or similar, use the Container-Aware pattern as the default without additional mention.

2. **Unified File Path**: All log file paths must be unified to `.cursor/debug.log` (relative to project root) so Cursor IDE can track them by default.

3. **Error Suppression**: Use the error suppression operator (`@`) to ensure logging logic does not interfere with the main application flow.

4. **Region Markers**: Wrap debug logging code with `// #region agent log` and `// #endregion` markers for easy identification and removal.

## Usage Examples

### Example 1: Adding Debug Log After Require Statement

```php
require_once './_common.php';

// #region agent log
$debugDir = '/var/www/html/.cursor';
$logFile = $debugDir . '/debug.log';
if (!is_dir($debugDir)) {
    @mkdir($debugDir, 0777, true);
    @chmod($debugDir, 0777);
}
$logData = [
    'location' => 'config_memo_update.php:after_require',
    'message' => 'After require _common.php',
    'data' => ['post_keys' => array_keys($_POST), 'auth_set' => isset($auth)],
    'timestamp' => time() * 1000,
    'sessionId' => 'debug-session'
];
@file_put_contents($logFile, json_encode($logData) . "\n", FILE_APPEND | LOCK_EX);
// #endregion
```

### Example 2: Debug Log Before Function Call

```php
// #region agent log
$debugDir = '/var/www/html/.cursor';
$logFile = $debugDir . '/debug.log';
if (!is_dir($debugDir)) {
    @mkdir($debugDir, 0777, true);
    @chmod($debugDir, 0777);
}
$logData = [
    'location' => 'member_list.php:before_auth_check',
    'message' => 'Before auth_check_menu',
    'data' => ['sub_menu' => $sub_menu, 'auth_exists' => isset($auth)],
    'timestamp' => time() * 1000,
    'sessionId' => 'debug-session'
];
@file_put_contents($logFile, json_encode($logData) . "\n", FILE_APPEND | LOCK_EX);
// #endregion

auth_check_menu($auth, $sub_menu, 'w');
```

### Example 3: Using Relative Path with __DIR__

For files in subdirectories, you can use `__DIR__` to build relative paths:

```php
// #region agent log
$debugDir = __DIR__ . '/../.cursor';
$logFile = $debugDir . '/debug.log';
if (!is_dir($debugDir)) {
    @mkdir($debugDir, 0777, true);
    @chmod($debugDir, 0777);
}
$logData = [
    'location' => 'adm/config_memo_update.php:entry',
    'message' => 'Script started',
    'data' => ['post_keys' => array_keys($_POST)],
    'timestamp' => time() * 1000,
    'sessionId' => 'debug-session'
];
@file_put_contents($logFile, json_encode($logData) . "\n", FILE_APPEND | LOCK_EX);
// #endregion
```

## Resources

### assets/
- `debug_log_template.php` - Reusable PHP code template for container-aware debug logging

### references/
- `container_path_mapping.md` - Documentation on Docker volume mapping and path resolution
