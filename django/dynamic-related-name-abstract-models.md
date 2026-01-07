# Dynamic related_name in Abstract Models

Django's abstract model inheritance supports template syntax for `related_name` that dynamically generates names based on the child class.

## How it works

-   `%(class)s` gets replaced with the lowercase name of the child model
-   `%(app_label)s` gets replaced with the app name

## Example

```python
class BaseComment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)ss",  # Template syntax
        on_delete=models.CASCADE,
    )
    content = models.TextField()

    class Meta:
        abstract = True


class ArticleComment(BaseComment):  # related_name becomes "articlecomments"
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class PhotoComment(BaseComment):  # related_name becomes "photocomments"
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
```

Usage:

```python
user.articlecomments.all()  # All article comments by user
user.photocomments.all()    # All photo comments by user
```

## Why it's needed

Without dynamic related names, both child models would try to use the same `related_name`, causing a Django error:

```
ERRORS: Reverse accessor clashes...
```

## Available placeholders

| Placeholder     | Result                                        |
| --------------- | --------------------------------------------- |
| `%(class)s`     | Lowercase model name (e.g., `articlecomment`) |
| `%(app_label)s` | App name (e.g., `blog`)                       |

You can combine them: `related_name="%(app_label)s_%(class)s_set"`
