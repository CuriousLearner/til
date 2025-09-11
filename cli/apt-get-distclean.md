# `apt-get distclean` for complete package cleanup

`apt-get distclean` is a comprehensive cleanup command that removes downloaded package files, partial packages, and cleans up the package cache more thoroughly than `apt-get clean`.

While `apt-get clean` only removes downloaded package files from the cache, `distclean` goes further by also removing partial packages and any other cached data that might be left behind.

## Usage:

```bash
sudo apt-get distclean
```

## What it does:

- Removes all downloaded package files from `/var/cache/apt/archives/`
- Removes partial package files from `/var/cache/apt/archives/partial/`
- Cleans up any other cached package data
- Frees up more disk space than `apt-get clean`

## Example:

```bash
# Check current cache size
du -sh /var/cache/apt/archives/

# Perform complete cleanup
sudo apt-get distclean

# Verify cleanup
du -sh /var/cache/apt/archives/
```

This is particularly useful when you need to free up maximum disk space or ensure a completely clean package cache state.
