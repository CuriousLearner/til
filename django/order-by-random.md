# Random ordering with order_by("?") in Django

Django provides a convenient way to retrieve records in random order using `order_by("?")`:

```python
# Get 5 random articles
random_articles = Article.objects.order_by("?")[:5]
```

This uses the database's random function to shuffle results:
- PostgreSQL: `RANDOM()`
- MySQL: `RAND()`
- SQLite: `RANDOM()`
- Oracle: `DBMS_RANDOM.VALUE()`

## Important considerations

**Performance**: Random ordering can be slow on large tables since it requires the database to generate a random value for each row and then sort them. For better performance on large datasets, consider these alternatives:

```python
import random

# Option 1: Random offset (works for small-ish result sets)
count = Article.objects.published().count()
random_offset = random.randint(0, max(0, count - 20))
articles = Article.objects.published()[random_offset:random_offset + 20]

# Option 2: Random IDs (better for large sets)
published_ids = list(Article.objects.published().values_list('id', flat=True))
random_ids = random.sample(published_ids, min(20, len(published_ids)))
articles = Article.objects.filter(id__in=random_ids)

# Option 3: Cache random IDs (best for hot paths)
# Cache the full ID list, sample from cache to avoid DB queries
```

**Consistency**: Each call to `order_by("?")` produces a different random order, so pagination won't work reliably with random ordering.

Use `order_by("?")` for small datasets or when you need truly random results and performance isn't critical.
