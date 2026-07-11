# Git's Three Layers of Ignore Rules

Git evaluates ignore rules from three sources, in order:

| Layer | File                                                 | Scope                           |
| ----- | ---------------------------------------------------- | ------------------------------- |
| 1     | `.gitignore`                                         | Committed, shared with everyone |
| 2     | `.git/info/exclude`                                  | Local clone only, never pushed  |
| 3     | `core.excludesFile` (usually `~/.config/git/ignore`) | All repos on this machine       |

## Layer 1 — `.gitignore`

The standard approach. Gets committed into the repo, so every collaborator picks up the same rules automatically.

Use this for things the whole team should ignore: build artefacts, `node_modules`, `*.pyc`, etc.

## Layer 2 — `.git/info/exclude`

Same syntax as `.gitignore`, but lives inside the `.git` directory, which is never committed or pushed. The rule only affects your local clone.

```
# .git/info/exclude
designs/
scratch.sql
```

Use this when you want to keep a folder in your working directory without leaving any trace of it in the repo history — not even the ignore rule itself. No collaborator will ever see it.

## Layer 3 — `core.excludesFile`

A machine-wide ignore file, applied to every repo you clone.

```bash
git config --global core.excludesFile ~/.config/git/ignore
```

Use this for editor artefacts and OS noise that are personal to your machine: `.DS_Store`, `.idea/`, `*.swp`, etc.

## How Ignored Paths Behave

Once a path matches any rule:

- `git add .` silently skips it.
- It cannot be staged accidentally (you need `git add -f` to force it).
- `git status --ignored` shows ignored paths with `!!` markers.
- `git check-ignore -v <path>` names the exact rule and file responsible.

```bash
$ git check-ignore -v designs/
.git/info/exclude:7:designs/   designs/
```

## Overriding a Global Rule for One Repo

Prefix the pattern with `!` in the repo's `.gitignore` to negate a global rule. Git processes all three layers together and the last matching rule wins.

```
# .gitignore
!designs/
```

**Catch:** negation doesn't work if a parent directory is already ignored. Git won't descend into an ignored directory to un-ignore things inside it. To carve out a subdirectory, un-ignore the parent first, re-ignore its contents, then add the exception:

```
# .gitignore
!scratch/
scratch/*
!scratch/important/
```

## Choosing the Right Layer

- Everyone should ignore it → `.gitignore`
- Only you should ignore it, privately, in this repo → `.git/info/exclude`
- Only you should ignore it, across all repos → `~/.config/git/ignore`
- Global rule, but not in this repo → negate with `!pattern` in the repo's `.gitignore`
