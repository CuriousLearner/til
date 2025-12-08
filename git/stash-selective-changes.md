# Stash Selective Changes in Git

Git allows stashing only staged or unstaged changes using `--staged` and `-k` (`--keep-index`). You can also stash specific files.

## Stash Only Staged Changes

```bash
git stash --staged
```

* Moves staged (indexed) changes to stash.
* Leaves unstaged changes in the working directory.

## Stash Only Unstaged Changes

```bash
git stash -k  # or --keep-index
```

* Moves unstaged changes to stash.
* Keeps staged changes for commit.

## Stash Selected Files

```bash
git stash push -m "stash message" -- path/to/file1 path/to/file2
```

* Stashes only the specified files.
* Allows adding a message for reference.
* Other changes remain untouched.
