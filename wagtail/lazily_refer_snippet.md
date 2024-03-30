# Lazily Refer Snippet in blocks

`SnippetChooserBlock` in Django Wagtail can cleverly sidestep circular dependencies. By lazily referring to a snippet, you can effectively dodge those pesky circular dependencies that can otherwise tangle up your code. Just set up your `SnippetChooserBlock` like this:

```python
from wagtail.snippets.blocks import SnippetChooserBlock

SnippetChooserBlock(target_model="app.ContentSnippet")
```

And watch as your code becomes cleaner and more maintainable! No more headaches trying to unravel circular dependencies.
