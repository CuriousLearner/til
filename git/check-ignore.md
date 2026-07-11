# `git check-ignore` — Debug Which Rule Is Ignoring a Path

`git check-ignore` tells you whether a path is ignored and, with `-v`, exactly which rule and file is responsible.

## Basic Usage

```bash
git check-ignore designs/
```

Exits 0 (ignored) or 1 (not ignored). No output by default — useful in scripts.

## `-v` — Verbose: Show the Winning Rule

```bash
$ git check-ignore -v designs/
.git/info/exclude:7:designs/    designs/
```

Output format: `<source-file>:<line-number>:<pattern>  <path>`

This tells you exactly which file and which line matched.

## `-v --verbose` with Multiple Paths

```bash
$ git check-ignore -v node_modules/ .DS_Store scratch.sql
.gitignore:3:node_modules/              node_modules/
/Users/you/.config/git/ignore:1:.DS_Store   .DS_Store
.git/info/exclude:8:scratch.sql         scratch.sql
```

Each path shows the layer it was matched in — handy for auditing which layer is responsible for what.

## `--no-index` — Check Tracked Files Too

By default, `git check-ignore` only checks untracked paths. If a file is already tracked, it won't report it as ignored even if a rule matches.

```bash
git check-ignore -v --no-index some/tracked/file.log
```

Useful when a file is accidentally tracked and you want to confirm the ignore rule exists before removing it from the index.

## Common Use Cases

**Why isn't this file being ignored?**

```bash
git check-ignore -v path/to/file
# no output = no rule matches it
```

**Which layer owns this ignore rule?**

```bash
git check-ignore -v node_modules/
# shows .gitignore, .git/info/exclude, or global ignore file
```

**Audit all ignored files in the repo:**

```bash
git status --ignored
# shows ignored paths with !! markers; check-ignore -v <path> for any you want to investigate
```
