# Revert file(s) state to one in diff branch

Often times, we come across a situation where we have made changes in our current branch and want to revert some files to the exact state they were in at a certain point in another branch (diff branch). This can be done using `git`'s powerful features.

```bash
git checkout <other-branch> -- <file-or-glob>...
```

To check for changes before a checkout, you can use:

```bash
git diff <commit-in-diff-branch> <file-or-glob>
```

Examples:

```bash
# Check 'README.md' diff from it's state in the master branch.
git diff master -- README.md
git checkout master -- README.md

# Revert 'README.md' to the state it was in branch 'feature-branch'
git checkout feature-branch -- README.md
```
