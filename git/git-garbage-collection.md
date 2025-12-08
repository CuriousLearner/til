# Git Garbage Collection

Use `git reflog expire` and `git gc` to permanently remove unreachable objects from your repository. Essential after rewriting history with filter-branch, reset, or rebase.

## Expire Reflog Entries

```bash
git reflog expire --expire=now --all
```

| Flag           | Purpose                                                |
| -------------- | ------------------------------------------------------ |
| `--expire=now` | Expire all entries immediately (default keeps 90 days) |
| `--all`        | Process reflogs of all references, not just HEAD       |

The reflog keeps a safety net of all ref updates. Expiring it removes references to old commits, making them eligible for garbage collection.

## Garbage Collect

```bash
git gc --prune=now --aggressive
```

| Flag           | Purpose                                                       |
| -------------- | ------------------------------------------------------------- |
| `--prune=now`  | Remove unreachable objects immediately (default: 2 weeks old) |
| `--aggressive` | More thorough optimization; slower but better compression     |

## Full Cleanup Sequence

After history-rewriting operations:

```bash
# 1. Remove filter-branch backups (if applicable)
rm -rf .git/refs/original/

# 2. Expire all reflog entries
git reflog expire --expire=now --all

# 3. Aggressively garbage collect
git gc --prune=now --aggressive
```

## When to Use

-   After `git filter-branch` to remove sensitive data
-   After `git reset --hard` to older commits
-   After deleting branches with large files
-   To reduce repository size before sharing

## Verify Objects Are Gone

```bash
# Check repository size before and after
du -sh .git

# List all objects (should not include removed commits)
git rev-list --all
```

## Important Notes

-   This is irreversible — unreachable objects cannot be recovered after gc
-   `--aggressive` can be slow on large repos; omit for routine cleanup
-   Remote repos retain their own objects until they run gc
