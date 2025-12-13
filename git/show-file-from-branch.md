# Show file contents from a specific branch

You can use `git show` to view a file's contents as they exist in a different branch without checking out that branch:

```bash
git show <branch>:<path/to/file>
```

## Example

```bash
git show feat/locations-geo-nearby:src/api/routers/locations.py
```

This displays the full contents of `src/api/routers/locations.py` as it exists on the `feat/locations-geo-nearby` branch.

## Redirecting stderr

Add `2>&1` to capture any error messages (like if the file doesn't exist on that branch) to stdout:

```bash
git show feat/locations-geo-nearby:src/api/routers/locations.py 2>&1
```

## Use cases

- Quickly inspect changes on another branch without switching branches
- Compare implementations between branches
- Extract specific file versions for review or debugging
