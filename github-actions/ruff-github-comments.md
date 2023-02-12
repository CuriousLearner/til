# Enable automatic inline annotations in PR using Ruff

To quickly see inline annotations from [ruff](https://github.com/charliermarsh/ruff) in your Github pull request, use `--format github` in Github Actions file like:

```yaml
name: CI
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ruff
      # Include `--format=github` to enable automatic inline annotations.
      - name: Run Ruff
        run: ruff check --format=github .
```
