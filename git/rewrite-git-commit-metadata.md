# Rewrite Git Commit Metadata

Use `git filter-branch --env-filter` to rewrite commit metadata (author name, email, dates) across your entire git history. Useful for fixing incorrect author info or standardizing commit metadata.

## Rewrite Using an External Script

```bash
FILTER_BRANCH_SQUELCH_WARNING=1 \
git filter-branch -f --env-filter 'source /path/to/fix-script.sh' -- --all
```

### Example Script: Fix Author and Committer

```bash
# /tmp/fix-author-date.sh

OLD_EMAIL="wrong@email.com"
NEW_NAME="Correct Name"
NEW_EMAIL="correct@email.com"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi

if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
```

## Available Environment Variables

The `--env-filter` can modify these variables:

| Variable              | Purpose                             |
| --------------------- | ----------------------------------- |
| `GIT_AUTHOR_NAME`     | Author's name                       |
| `GIT_AUTHOR_EMAIL`    | Author's email                      |
| `GIT_AUTHOR_DATE`     | When the change was originally made |
| `GIT_COMMITTER_NAME`  | Committer's name                    |
| `GIT_COMMITTER_EMAIL` | Committer's email                   |
| `GIT_COMMITTER_DATE`  | When the commit was created         |

## Cleanup After Filtering

```bash
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

## Important Notes

-   Author != Committer: Author wrote the code; Committer applied it (e.g., via cherry-pick)
-   This rewrites history — force push required: `git push --force --all`
-   All commit hashes will change
