<?php
/**
 * Container-Aware Debug Log Template
 * 
 * This template provides a reusable pattern for adding debug logging
 * that works in both Docker container and host environments.
 * 
 * Usage: Copy this code block and customize the location, message, and data fields.
 */

// #region agent log
// 1. Path definition: Specify .cursor folder within the shared volume
$debugDir = '/var/www/html/.cursor'; // Container-mounted volume path
$logFile = $debugDir . '/debug.log';

// 2. Environment preparation: Create directory if missing (prevents Permission Error)
if (!is_dir($debugDir)) {
    @mkdir($debugDir, 0777, true);
    @chmod($debugDir, 0777); 
}

// 3. Logging execution: Maintain JSON format and apply exclusive lock (LOCK_EX)
$logData = [
    'location' => '{FILE_NAME}:{LINE_OR_MARKER}',  // e.g., 'config_memo_update.php:after_require'
    'message' => '{DESCRIPTIVE_MESSAGE}',          // e.g., 'After require _common.php'
    'data' => [                                    // Custom data array
        // Add relevant debugging data here
    ],
    'timestamp' => time() * 1000,                  // Milliseconds since epoch
    'sessionId' => 'debug-session'                 // Optional: session identifier
];
@file_put_contents($logFile, json_encode($logData) . "\n", FILE_APPEND | LOCK_EX);
// #endregion
