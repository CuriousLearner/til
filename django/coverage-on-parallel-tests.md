# Fixing Coverage for Django's `manage.py test --parallel`

Running `manage.py test --parallel` **dropped coverage** significantly, even though all tests passed. After debugging, I found the following key fixes:

## 1. Enable Coverage for Subprocesses

Django **spawns subprocesses** for parallel tests, but coverage wasn’t tracking them. To fix this, I enabled **`coverage.process_startup()`**, which ensures coverage runs in every spawned process:

- **Manual Method (For Normal Projects)**:
  Add this to `sitecustomize.py`:

  ```python
  import coverage
  coverage.process_startup()
  ```

- **Better Alternative (What I Used)**:

    Instead of modifying `sitecustomize.py`, install:

    ```bash
    pip install coverage_enable_subprocess
    ```

    This automatically enables coverage tracking in all subprocesses. This is specially useful for Django case when you won't to spend time in configuring `PYTHONPATH` and ensuring `sitecustomize` load before `django.load()` It took a while to figure this out.

    Save yourself time, and install this.

## 2. Properly Configuring `.coveragerc`

I updated `.coveragerc` to explicitly enable multiprocessing:

```
[run]
parallel = True
concurrency = multiprocessing
source = src
dynamic_context = test_function
```

## 3. Fixing coverage combine Issues

Since coverage runs separately in each parallel process, it generates multiple `.coverage` files. I had to explicitly combine them:

```bash
coverage combine /tmp/coverage/
coverage report -m
coverage xml -o /tmp/coverage/coverage.xml
```

## 4. Exporting `COVERAGE_PROCESS_START`

To ensure subprocesses use the correct coverage config, I set:

```bash
export COVERAGE_PROCESS_START=.coveragerc
```

This ensures all spawned test processes follow `.coveragerc` settings.

## 5. Removing `--append` from `coverage run`

Earlier, `coverage run --append` caused conflicts in parallel mode. Instead, I now let coverage combine handle merging.

## 6. Ensuring Coverage Files are Properly Named

Each test run was generating `.coverage.<hostname>.<random_id>`, and combining them correctly was crucial. I confirmed they were stored in `/tmp/coverage/`.


## Conclusion

Combined examples from various sources to fix coverage issues with Django's parallel tests.

```bash
NPROC := $(shell if command -v nproc >/dev/null; then nproc; else sysctl -n hw.ncpu; fi)
COVERAGE_FILE=/tmp/coverage/.coverage.$(hostname).$$RANDOM \
COVERAGE_PROCESS_START=.coveragerc \
coverage run --source=src \
src/manage.py test --parallel $(NPROC) --keepdb --no-input && \
coverage combine /tmp/coverage/ && \
coverage report -m && \
coverage xml -o /tmp/coverage/coverage.xml
```

Now, coverage remains stable even when running tests in parallel.
