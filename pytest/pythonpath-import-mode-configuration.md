# Understanding pytest pythonpath and import-mode configuration

## What `pythonpath` does

The `pythonpath` configuration option modifies `sys.path` by adding specified directories to Python's module search path:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
```

- Adds directories to `sys.path` relative to the rootdir
- Useful for src layout projects or avoiding PYTHONPATH environment variables
- Available since pytest 7.0.0
- Keeps path configuration in the repo and distributes to other developers

## `pytest` vs `python -m pytest` difference

### `python -m pytest`:
- Automatically adds the current directory to `sys.path`
- Standard Python behavior when running modules with `-m`
- More reliable for local development without installed packages

### `pytest` command:
- Relies on existing Python environment configuration
- Uses pytest's own import mechanisms (prepend mode by default)
- Assumes modules are properly installed or `sys.path` is configured

## What `--import-mode=importlib` does

```toml
[tool.pytest.ini_options]
addopts = "--import-mode=importlib"
```

- Circumvents the standard Python way of using modules and `sys.path`
- Doesn't modify `sys.path` or `sys.modules` during test discovery
- Allows test modules to have non-unique names
- Makes behavior less surprising but has some trade-offs
- Uses Python's importlib instead of modifying the module system

The `pythonpath` option essentially provides what `python -m pytest` does automatically - ensuring your local modules are discoverable during testing.
