# Using pkill with -f flag for full command line matching

The `-f` flag in `pkill` matches against the entire command line, not just the process name.

## Basic pkill vs pkill -f

```bash
# Only matches process name "python"
pkill python

# Matches full command line containing "manage.py runserver"
pkill -f "manage.py runserver"
```

## Why it's useful for Django development

When you run Django's development server:
```bash
python manage.py runserver
```

The actual process name is `python`, not `runserver`. Without `-f`, you'd kill all Python processes:

```bash
# Dangerous - kills ALL python processes
pkill python

# Safe - only kills Django runserver
pkill -f "manage.py runserver"
```

## How -f works

The `-f` flag tells `pkill` to match the pattern against the full command line shown in `ps aux`:

```bash
# See what would be matched
ps aux | grep "manage.py runserver"

# Kill those specific processes
pkill -f "manage.py runserver"
```

## Other useful flags

```bash
# Check what would be killed (dry run)
pgrep -f "manage.py runserver"

# Kill with specific signal
pkill -f -TERM "manage.py runserver"

# Case insensitive matching
pkill -f -i "MANAGE.py runserver"
```

## Common use cases

```bash
# Kill specific Django port
pkill -f "runserver 0.0.0.0:8000"

# Kill Celery workers
pkill -f "celery worker"

# Kill specific pytest runs
pkill -f "pytest tests/unit"

# Kill Jupyter notebooks
pkill -f "jupyter-notebook"
```