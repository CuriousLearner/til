# Update dependencies in requirements.txt

You can use `pur` to update all dependencies in a requirements file like:

```bash
pur -r requirements.txt
```

`pur` never modifies your environment or installed packages, it just updates the txt file with latest dependencies. So you can install requirements with `pip install -r requirements.txt`, afterwards.
