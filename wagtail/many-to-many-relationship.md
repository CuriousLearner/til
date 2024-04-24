# Many to Many relationship in Wagtail

A Many-to-Many relationship can be implemented using a `ParentalManyToManyField` in Wagtail. This field is designed for use within a `PageModel` and allows you to create a many-to-many relationship between different pages. The `ParentalManyToManyField` allows the relations between m2m linked objects to be stored in memory without writing to the database.

```python
from modelcluster.fields import ParentalManyToManyField
```

You can then define the `ParentalManyToManyField` in your Wagtail model, specifying the related page model that you want to establish the many-to-many relationship with.

**Caveat**: If you're using snippets, make sure the snippet is using the `ParentalManyToManyField`, otherwise it won't render correctly with `FieldPanel`. Furthermore, the snippet cannot inherit from `models.Model`, otherwise the m2m relationship will not be saved. They should inherit from `modelcluster.models.ClusterableModel` instead.

```python
from modelcluster.fields import ParentalManyToManyField
from modelcluster.models import ClusterableModel

from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class MySnippet(ClusterableModel):
    my_pages = ParentalManyToManyField(Page, related_name="+")
```

This will create a many-to-many relationship between the `MySnippet` model and the `Page` model.
