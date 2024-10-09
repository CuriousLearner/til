# `paths` and `paths-ignore` filter for optimized Workflow run

If you need your Github Actions to run only when changes happen to specific directories or files, you can add a `paths` filter in Github Actions like:

```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'scripts/**'
```

This triggers the workflow if any changes are made in either the `src/` or `scripts/` directories.

Similarly, there is also `path-ignore` which can be used as:

```yaml
on:
  push:
    paths-ignore:
      - 'docs/**'
      - '*.md'
```

This will prevent the workflow from running when only changes to markdown files (`*.md`) or files inside the `docs/` folder are made.
