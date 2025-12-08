# Editable installation for a package

Just learned about editable installation in Python! It's a way to install a package in 'editable' mode, which means you can make changes to the package and see the changes reflected immediately without reinstalling it.

```bash
pip install -e .
```

In poetry, you can use the `path` option with `develop` as `true` to install a package in editable mode. This is useful when you want to develop a package and see the changes reflected immediately without reinstalling it.

```bash
pacakge = {path= "/path/to/package", develop = true}
```

With poetry, you can also use the `--editable` flag to install a package in editable mode.

```bash
poetry add --editable /path/to/package
```
