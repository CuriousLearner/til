# Redundant all chaining in queryset

The default queryset from manager includes all the objects already. So, in most cases, `.all()` call can be avoided while chaining querysets.

For example:

```python
Post.objects.all().filter(title__startswith='Cool post')
```

can be trimmed down to:

```python
Post.objects.filter(title__startswith='Cool post')
```

The only reason to chain from `.all()` is for `delete()`, as a safeguard to ensure you really mean to delete everything: `Post.objects.all().delete()`.
