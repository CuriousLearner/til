# `git log --diff-filter` — Find Commits by Change Type

`--diff-filter` lets you filter `git log` to only show commits where files were changed in a specific way (deleted, added, renamed, etc.).

## Find Commits That Deleted a File

```bash
git log --oneline --diff-filter=D --name-only
```

Output:

```
a3f9c12 remove legacy payment handler
payments/legacy.py

8b2e001 clean up old migrations
migrations/0003_old.py
migrations/0004_old.py
```

The `--name-only` flag prints the affected file names below each commit.

## Recover a Deleted File

The common use case: you realise a file is gone and want to find the commit that deleted it, then restore it.

```bash
# 1. Find the commit that deleted the file
git log --oneline --diff-filter=D --name-only -- path/to/file.py

# 2. Restore it from the commit just before the deletion
git checkout <commit-hash>^ -- path/to/file.py
```

The `^` suffix means "the parent of that commit" — i.e. the last state where the file still existed.

## Filter Letters

| Flag | Meaning  |
| ---- | -------- |
| `D`  | Deleted  |
| `A`  | Added    |
| `M`  | Modified |
| `R`  | Renamed  |
| `C`  | Copied   |
| `U`  | Unmerged |

Combine multiple filters — `--diff-filter=DR` shows commits that deleted **or** renamed files.

Lowercase letters exclude instead of include — `--diff-filter=d` shows commits that did **not** delete any file.

## Scope to a Specific File

```bash
git log --oneline --diff-filter=D -- payments/legacy.py
```

The `--` separates git options from the file path and avoids ambiguity with branch names.
