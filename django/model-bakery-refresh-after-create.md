# Using `_refresh_after_create` in model_bakery

When using [model_bakery](https://github.com/model-bakers/model_bakery) to create test fixtures that involve models with special behaviors like `DirtyFieldsMixin`, you might need to refresh the instance from the database after creation to ensure tracking mechanisms are properly initialized.

Instead of manually calling `refresh_from_db()`:

```python
from model_bakery import baker

dm = baker.make(
    MyModel,
    name="Original Name",
)
# Refresh to ensure DirtyFieldsMixin tracking is reset after creation
dm.refresh_from_db()
```

You can use the `_refresh_after_create` parameter:

```python
dm = baker.make(
    MyModel,
    name="Original Name",
    _refresh_after_create=True,
)
```

This parameter automatically refreshes the instance from the database after creation, which is particularly useful when:
- Working with models that use `DirtyFieldsMixin` or similar tracking mechanisms
- Ensuring database-generated values (like auto-generated fields) are properly loaded
- Testing models with custom save methods that modify data during creation

The `_refresh_after_create=True` approach is cleaner and more declarative, making the intent clear while reducing boilerplate code in your tests.
