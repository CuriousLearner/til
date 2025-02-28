# Generate requirements without hashes

When using Docker, you can export dependencies to a `requirements.txt` file without hashes to decrease time to resolve dependencies.

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
