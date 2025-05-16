# `caplog` vs `syslog` in pytest – What’s the Difference?

When testing logging in `pytest`, you might come across `caplog` and `syslog`. Both capture logs, but they serve different purposes.

## 1️⃣ `caplog` – Captures Logs in pytest
Use `caplog` to **intercept logs** emitted by your code and assert on them.

```python
import logging
import pytest

def my_function():
    logging.getLogger("myapp").warning("Something went wrong!")

def test_logging(caplog):
    with caplog.at_level(logging.WARNING):
        my_function()
    assert "Something went wrong!" in caplog.text  # ✅ Captures log output
```

🔹 **Use case:** Checking if a function logs expected messages.
🔹 **Works within pytest only** (not system-wide).

## 2️⃣ `syslog` – Captures System Logs
`syslog` refers to **actual system-wide logs**, which pytest doesn’t capture by default. If your app logs to system `syslog`, you need to **redirect it manually** for testing.

```python
import subprocess

def test_syslog():
    logs = subprocess.check_output(["journalctl", "-n", "10"]).decode()
    assert "CRITICAL ERROR" not in logs  # ✅ Checks system logs
```

🔹 **Use case:** Monitoring system logs (e.g., `/var/log/syslog`).
🔹 **Not pytest-specific** – It’s for OS-level logging.

## TL;DR
✅ **Use `caplog` for pytest assertions** on logs inside Python.
❌ **`syslog` is system-wide** and needs manual handling in tests.

If you’re testing Python logs, **stick to `caplog`** – it’s built for pytest! 🚀
