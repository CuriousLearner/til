# `timedelta.total_seconds()` vs `timedelta.seconds` – A Critical Difference

When working with Python's `timedelta` objects, there's a critical difference between `.seconds` and `.total_seconds()` that can lead to subtle bugs.

## The Problem

- `.seconds` – Returns **only the seconds component** (0-86399) of the timedelta, excluding days
- `.total_seconds()` – Returns the **total duration** in seconds as a float

## Example

```python
from datetime import timedelta

# A duration of 2 days and 5 seconds
td = timedelta(days=2, seconds=5)

print(td.seconds)          # Output: 5 (only the seconds component!)
print(td.total_seconds())  # Output: 172805.0 (2 days + 5 seconds = 172800 + 5)
```

## Common Bug Pattern

```python
# WRONG - This only checks the seconds component
if some_timedelta.seconds > 3600:
    # This will NEVER trigger for durations like "2 days"
    # because .seconds only returns 0-86399
    do_something()

# CORRECT - This checks the entire duration
if some_timedelta.total_seconds() > 3600:
    do_something()
```

## Why This Matters

A timedelta has three components: `days`, `seconds`, and `microseconds`. The `.seconds` attribute only gives you the middle component (normalized to 0-86399), while `.total_seconds()` converts the entire duration to seconds.

## Rule of Thumb

**Always use `.total_seconds()` when you need the complete duration.** Only use `.seconds` when you specifically need just the seconds component of a time interval.
