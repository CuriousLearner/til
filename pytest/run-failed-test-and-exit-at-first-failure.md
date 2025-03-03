# Run only failed tests and stop at first failure in pytest

Use `pytest -x --lf` to speed up debugging:

* `--lf (last failed)` runs only the tests that failed in the previous run.
* `-x (exit first)` stops execution at the first failure.

If all tests passed in the last run, `--lf` runs all tests as a fallback.

Useful for quickly iterating on failing tests without running the entire test suite.
