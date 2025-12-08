# Isolate Redis cache for parallel tests

When running Django tests in parallel, the default Redis cache can cause issues. To avoid conflicts, you can isolate the cache for each test worker.

Here's how you can set up a unique cache for each worker:

1. **Update `CACHES` in `settings/testing.py`**:

```python
if ENVIRONMENT not in ["staging", "production"]:
    # Get unique Redis DB for each test worker
    worker_id = os.getenv("DJANGO_TEST_PROCESSES", "1")  # Django assigns a worker number
    redis_db = int(worker_id) % 16  # Redis has databases 0-15 by default

    CACHES["test"] = {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://redis:6379/{redis_db}",  # Assign unique DB for parallel test isolation
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }

```

2. **Run tests with `DJANGO_SETTINGS_MODULE=settings.testing`**:

   ```bash
    DJANGO_SETTINGS_MODULE=settings.testing ./manage.py test --parallel
    ```

`DJANGO_TEST_PROCESSES` is set by Django to assign a unique worker number for each test process. We use this to calculate a unique Redis database number for each worker.

Now, each test worker will use a separate Redis cache, preventing conflicts during parallel test runs.
