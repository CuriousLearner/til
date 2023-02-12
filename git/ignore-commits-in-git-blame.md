# Ignore commits in git-blame view

> All revisions specified in the .git-blame-ignore-revs file, which must be in the root directory of your repository, are hidden from the blame view using Git's `git blame --ignore-revs-file` configuration setting.

The file can look like this, preferrably should always have comments:

```bash
# .git-blame-ignore-revs
# Removed semi-colons from the entire codebase
a8940f7fbddf7fad9d7d50014d4e8d46baf30592
# Converted all JavaScript to TypeScript
69d029cec8337c616552756310748c4a507bd75a
```

Optionally, specify path for this ignore-revs-file, like:

```bash
git blame --ignore-revs-file .git-blame-ignore-revs
```

You can also configure your local git so it always ignores the revs in that file:

```bash
git config blame.ignoreRevsFile .git-blame-ignore-revs
```
