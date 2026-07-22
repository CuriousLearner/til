# `git rebase --onto` — Surgically Excise a Middle Commit

## The general form

```
git rebase --onto <newbase> <upstream> <branch>
```

- `<branch>` = the branch to rewrite (git checks it out first).
- `<upstream>` = a commit whose descendants get replayed. The replayed set is exactly `<upstream>..<branch>` (commits reachable from `<branch>` but **not** from `<upstream>`).
- `<newbase>` = the commit to replant those replayed commits onto.

Read it as: "take the commits **after** `<upstream>` up to `<branch>`, and reattach them **onto** `<newbase>`."

## Applied to a concrete case

Say we want to drop the bad commit `ccccccc` from the middle of `master`:

```
git rebase --onto bbbbbbb ccccccc master
```

History before:

```
aaaaaaa ── bbbbbbb ── ccccccc ── ddddddd   (master)
                       (bad)      (keep)
```

- `ccccccc..master` = everything on master not in `ccccccc` = just **`ddddddd`**. That's the set to replay.
- `--onto bbbbbbb` = replant that set starting from `bbbbbbb`.

git cherry-picks `ddddddd` onto `bbbbbbb`, producing a new commit `eeeeeee` (new SHA because its parent changed), and moves `master` there:

```
aaaaaaa ── bbbbbbb ── eeeeeee   (master)
                       (was ddddddd)
```

`ccccccc` is **left out**: as the `<upstream>` boundary it's not in the replayed range, and the replayed commit now hangs off `bbbbbbb`. Nothing points at `ccccccc` anymore, so it drops out of history.

## Why not plain `git rebase`

The two-arg `git rebase ccccccc` replays `ccccccc..master` **onto `ccccccc` itself**, which keeps it. `--onto` is what lets you replant onto a *different* base. Point `newbase` at the commit *before* the one you want gone and `upstream` at the commit itself, and the middle commit is excised.

Mnemonic: **`--onto NEW OLD`** = "move the stuff after OLD onto NEW; OLD gets left behind."

## Excising multiple commits at once

Same command, wider gap. The excised set is exactly `<newbase>..<upstream>`, so to drop a **contiguous block** point `<upstream>` at the newest commit in the block and `<newbase>` at the commit just before the block:

```
aaaaaaa ── bbbbbbb ── ccccccc ── ddddddd ── eeeeeee   (master)
            └──────── drop these ────────┘
```

```
git rebase --onto aaaaaaa ddddddd master
```

`ddddddd..master` = just `eeeeeee`, which gets replanted onto `aaaaaaa`. Everything in `aaaaaaa..ddddddd` (that's `bbbbbbb`, `ccccccc`, `ddddddd`) is left behind. The single-commit case is just the narrowest version of this, where `<newbase>` is the direct parent of `<upstream>`.

The catch: this only works for a **contiguous** range, because it's defined by two boundary commits. To drop non-adjacent commits (say `bbbbbbb` and `ddddddd` but keep `ccccccc`), use `git rebase -i` and delete those lines instead.
