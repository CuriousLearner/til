# `npm ci` (clean install) for CI pipelines

Just learned about `npm ci` command! It stands for 'clean install' and is super useful for Continuous Integration setups. Unlike `npm install`, it skips the dependency resolution step by using the existing `package-lock.json` or `npm-shrinkwrap.json`. This ensures faster, consistent builds with exact dependencies.

```bash
npm ci
```
