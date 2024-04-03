# Run tests that match substring in their name

You can filter and run only tests that contain or do not contain some substring in their name.

Examples:

```bash
# run all tests that contain `auth` in their name
$ pytest -k auth

# run all tests that do not contain `auth` in their name
$ pytest -k 'not auth'
```
