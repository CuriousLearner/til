# Bash trap with ERR and EXIT for Error Handling

The `trap` command in bash allows you to catch signals and execute code when certain events occur. It's particularly useful for cleanup operations and error notifications.

## Basic Syntax

```bash
trap 'command_to_execute' SIGNAL1 SIGNAL2 ...
```

## Understanding ERR and EXIT

### ERR Signal

-   Triggered when a command returns a non-zero exit status (fails)
-   Only works when `set -e` is enabled or `set -E` for functions
-   Does NOT trigger for commands in conditional statements (if, while, &&, ||)

### EXIT Signal

-   Always triggered when the script exits, regardless of success or failure
-   Executes after ERR trap if both are set
-   Perfect for cleanup operations

## Example: Error Notification Pattern

```bash
#!/bin/bash
SCRIPT_SUCCESS=false

function notify_error {
    if [ "$SCRIPT_SUCCESS" = false ]; then
        echo "Script failed, notifying Sentry..."
        curl -s "${SENTRY_CRONS}?status=error" || true
    fi
}

# Trap both ERR and EXIT
trap notify_error ERR EXIT

# Your script logic here
do_something_that_might_fail

# If we reach here, mark as successful
SCRIPT_SUCCESS=true
```

## How It Works

1. **ERR trap**: If any command fails (returns non-zero), the trap function executes immediately
2. **EXIT trap**: When the script exits (normally or due to error), the trap function executes
3. The combination ensures notification happens whether the script:
    - Fails at any point (ERR triggers, then EXIT)
    - Completes successfully (only EXIT triggers, but `SCRIPT_SUCCESS=true` prevents notification)
    - Is interrupted with Ctrl+C (EXIT still triggers)

## Exit Status Codes

-   `0`: Success
-   `1-255`: Various error conditions
-   `$?`: Contains the exit status of the last command

## Best Practices

1. Use `|| true` after non-critical commands in trap functions to prevent infinite loops
2. Set flags like `SCRIPT_SUCCESS` to differentiate between normal and error exits
3. Always use EXIT trap for cleanup (removing temp files, releasing locks)
4. Use ERR trap for immediate error handling

## Advanced Example

```bash
#!/bin/bash
set -eE  # Exit on error, ERR trap inherits to functions

TEMP_FILE=$(mktemp)
LOCK_FILE="/var/run/myapp.lock"

cleanup() {
    echo "Cleaning up..."
    rm -f "$TEMP_FILE"
    rm -f "$LOCK_FILE"
}

error_handler() {
    echo "Error on line $LINENO: Command '$BASH_COMMAND' failed with exit code $?"
    # Additional error reporting
}

trap cleanup EXIT
trap error_handler ERR

# Create lock file
touch "$LOCK_FILE"

# Main script logic
process_data > "$TEMP_FILE"
upload_results "$TEMP_FILE"

echo "Script completed successfully"
```

## Key Differences

| Aspect          | ERR                  | EXIT                  |
| --------------- | -------------------- | --------------------- |
| When triggered  | On command failure   | Always on script exit |
| Use case        | Error handling       | Cleanup operations    |
| Execution order | First (if error)     | Always last           |
| Works with      | `set -e` or `set -E` | Always works          |
