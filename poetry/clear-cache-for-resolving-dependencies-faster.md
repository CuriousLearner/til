# Clear cache for resolving dependencies faster

Well, I know caches are there for faster access. Unfortunately, poetry has a bug that is likely related to clearing out partial/incomplete/corrupted by concurrent usage downloads that can cause an indefinite hang while resolving dependencies.

If we clear the cache, it would be able to resolve dependencies faster.

Use the following command for clearing the cache:

```bash
poetry cache clear --all pypi
```

More [information on Github issue here](https://github.com/python-poetry/poetry/issues/2094#issuecomment-1248526469)
