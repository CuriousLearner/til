# Remove lines matching a pattern

You can use `grep -v`, but let's do this in vim with Vim’s powerful "global" command, `:g` for short as:

- `:g/pattern/d` – Remove lines matching pattern
- `:g!/pattern/d` – Remove lines that **do NOT** match the pattern
- `:v/pattern/d` – Also removes lines that **do NOT** match the pattern
