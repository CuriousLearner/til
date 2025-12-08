# Finding Git Commits That Touched a Specific File or String

When working with **Git**, you may need to track changes to a file or find when a specific option (e.g., `-j` in a `Makefile`) was introduced or modified. Here are some useful commands:


| Use Case                                          | Command                                               |
| ------------------------------------------------- | ----------------------------------------------------- |
| Show full commit history for a file               | `git log --follow -- Makefile`                        |
| Show commit history with diffs                    | `git log --follow -p -- Makefile`                     |
| Show only commits that added/removed `-j`         | `git log --follow -S'-j' -- Makefile`                 |
| Show full details of commits affecting `-j`       | `git log --follow -S'-j' -p -- Makefile`              |
| Find first commit that introduced `-j`            | `git log --follow --diff-filter=A -S'-j' -- Makefile` |
| Show only the added/removed lines containing `-j` | `git log --follow -p -- Makefile \| grep --color -E '^-.*-j \|^\+.*-j'` |

**Key Flags Explained**:

-   `--follow` - Continues tracking history even if the file was renamed.
-   `-p` - Shows diffs (code changes).
-   `-S'<string>'` - Finds commits where `<string>` was added or removed.
-   `--diff-filter=A` - Finds the commit where the file or string first appeared.
