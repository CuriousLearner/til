# Remove Files from Git History

Use `git filter-branch --index-filter` to completely remove files from your entire git history. This is useful for removing accidentally committed secrets, large files, or sensitive data.

## Remove a File from All History

```bash
git filter-branch -f --index-filter \
  'git rm --cached --ignore-unmatch FILENAME' \
  --prune-empty -- --all
```

### Flags Explained

| Flag               | Purpose                                                            |
| ------------------ | ------------------------------------------------------------------ |
| `-f`               | Force run, even if a backup from a previous filter-branch exists   |
| `--index-filter`   | Operates on the index (staging area) — faster than `--tree-filter` |
| `--cached`         | Remove from index only, not working directory                      |
| `--ignore-unmatch` | Don't fail if file doesn't exist in some commits                   |
| `--prune-empty`    | Remove commits that become empty after filtering                   |
| `-- --all`         | Apply to all branches and tags                                     |

## Suppress the Warning

Git shows a warning that `filter-branch` has pitfalls. Suppress it with:

```bash
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch ...
```

## Cleanup After Filtering

After filter-branch, old objects still exist. Clean them up:

```bash
# Remove backup refs created by filter-branch
rm -rf .git/refs/original/

# Expire all reflog entries
git reflog expire --expire=now --all

# Aggressively garbage collect
git gc --prune=now --aggressive
```

## Important Notes

-   This rewrites history — force push required: `git push --force --all`
-   Coordinate with team members; they'll need to re-clone or rebase
-   Consider using `git-filter-repo` (faster, recommended by Git) for large repos
