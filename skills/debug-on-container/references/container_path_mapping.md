# Docker Container Path Mapping Reference

## Standard Volume Mapping (from compose.yml)

In Docker Compose configurations, the host project root is typically bind-mounted to a container path via `compose.yml`. For example:

```yaml
services:
  web:
    volumes:
      - ./:/var/www/html
```

From this mapping:
- Host path: `./` (project root on the host, e.g. `/home/ubuntu/rainbow_2025/`)
- Container path: `/var/www/html/` (project root inside the container)
- Shared files: Both environments see the same files under their respective roots

## Path Resolution Strategy

### Problem
When PHP code runs inside a container, absolute paths like `/home/ubuntu/rainbow_2025/.cursor/debug.log` don't exist in the container's filesystem. The container only knows about `/var/www/html/`.

### Solution
Use container-relative paths based on the container root discovered from `compose.yml`:
- ✅ `<containerRoot>/.cursor/debug.log` (e.g. `/var/www/html/.cursor/debug.log`)
- ❌ `<hostRoot>/.cursor/debug.log` (e.g. `/home/ubuntu/rainbow_2025/.cursor/debug.log`, host-only path)

When present, always prefer reading `compose.yml` to determine:
- `hostRoot`  = left-hand side of the volume mapping (e.g. `./`)
- `containerRoot` = right-hand side of the volume mapping (e.g. `/var/www/html`)

## Alternative Path Patterns

### Using __DIR__ for Relative Paths

For files in subdirectories, you can use `__DIR__` to build paths relative to the current file:

```php
// If file is at: /var/www/html/adm/config_memo_update.php
$debugDir = __DIR__ . '/../.cursor';  // Resolves to /var/www/html/.cursor
$logFile = $debugDir . '/debug.log';
```

### Using Project Root Constants

If your project defines a root constant (e.g., `G5_PATH`), use it:

```php
$debugDir = G5_PATH . '/.cursor';
$logFile = $debugDir . '/debug.log';
```

## Permission Considerations

### Directory Creation
Always check and create the log directory before writing:

```php
if (!is_dir($debugDir)) {
    @mkdir($debugDir, 0777, true);  // Recursive creation
    @chmod($debugDir, 0777);        // Explicit permissions
}
```

### Why 0777?
- Container environments may have different user/group mappings
- 0777 ensures write access regardless of container user
- Error suppression (`@`) prevents failures from breaking main flow

## File Locking

Use `LOCK_EX` flag to prevent concurrent write issues:

```php
@file_put_contents($logFile, $content, FILE_APPEND | LOCK_EX);
```

This ensures:
- Atomic writes
- No corruption from concurrent processes
- Safe multi-process logging

## Cursor IDE Integration

Cursor IDE tracks `.cursor/debug.log` by default. Using this standardized path ensures:
- Automatic log file detection
- Easy log viewing in IDE
- Consistent debugging workflow
