# Using `add_q` in Django Queries

In Django, the `add_q` method is part of the internal QuerySet API and is used to combine complex query conditions using Q objects. It allows you to dynamically build and combine queries with logical operators.

```python
from django.db.models import Q
from myapp.models import MyModel

# Create an initial queryset
qs = MyModel.objects.all()

# Create Q objects for complex conditions
q1 = Q(name__icontains='example')
q2 = Q(age__gte=18) | Q(city='New York')

# Use add_q to combine conditions
qs.query.add_q(q1)
qs.query.add_q(q2)

# Evaluate the final queryset
results = qs.all()
```

This will be an implicit `AND` between `q1` and `q2`, meaning it will return rows where both conditions are true. You can also explicitly use `Q.And` for an `AND` or `Q.Or` for an `OR`.
