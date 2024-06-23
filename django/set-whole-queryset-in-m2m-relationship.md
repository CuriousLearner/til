# Add Multiple Objects In Queryset In Many To Many Relationship

In Django, to add multiple objects in a many-to-many relationship, use the `set()` method. This replaces current related objects with a new set.

For example, with models Ad and Newsletter having a many-to-many relationship via newsletter:

```python
new_ad.newsletter.set(original_ad.newsletter.all())
```

**NOTE**: This sets new_ad's newsletters to be the same as original_ad's. No need for `.save()` after `.set()`.
