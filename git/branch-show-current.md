# git branch --show-current

A clean way to get the name of the current branch:

```bash
git branch --show-current
```

```
main
```

This was added in Git 2.22 (June 2019). Before this, the common workarounds were:

```bash
git rev-parse --abbrev-ref HEAD

# or
git symbolic-ref --short HEAD
```

The key difference: `--show-current` prints nothing (with a zero exit code) when in a detached HEAD state, while `rev-parse --abbrev-ref HEAD` prints `HEAD` and `symbolic-ref` errors out. This makes `--show-current` safer to use in scripts where you want to handle detached HEAD separately:

```bash
branch=$(git branch --show-current)
if [ -z "$branch" ]; then
  echo "Detached HEAD — not on any branch"
else
  echo "On branch: $branch"
fi
```

Useful in shell aliases, prompts, and CI scripts where you need the branch name as a string.
