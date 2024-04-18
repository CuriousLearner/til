# `git diff --name-only` for file names only

`git diff --name-only` is a command used in Git, a distributed version control system. This command compares the working directory with the staging area (index) and outputs the names of files that have changed.

The `--name-only` flag is used to show only the names of the files that have changed, without any additional information. This can be useful when you want to see a list of files that have been modified, added, or deleted.

Here is an example of how to use `git diff --name-only`:

```bash
git diff --name-only
```

This will output a list of file names that have changed between the working directory and the staging area.

Alternate usage:

```bash
git diff --name-only HEAD~1 HEAD
```

This will output a list of file names that have changed between the current commit and the previous commit.

```bash
git diff --name-only <commit1> <commit2>
```

or

```bash
git diff --name-only <branch1> <branch2>
```
