# Get blocks in StreamBlock using blocks_by_name, first_block_by_name

If you're using a StreamField, you can access the blocks using the `blocks_by_name` method. This will return a list of the blocks with the given name.

Example:

```python
@register_snippet
class Menu(models.Model):

    content = StreamField(
        [
            ("column", ContentColumnBlock()),
            ("sidebar", SidebarBlock()),
        ]
    )
    def clean(self):
        super().clean()
        if len(self.content.blocks_by_name("sidebar")) > 1:
            raise ValidationError("Only one sidebar block is allowed.")
        for column_block in self.content.blocks_by_name("column"):
            if len(column_block.value["column"]) > 3:
                raise ValidationError(
                    "Only up to three choices in each column is allowed."
                )
```

You can also use the `first_block_by_name` method if you only want to get the first block with the given name.

Example:

```python
{{ menu.content.blocks.first_block_by_name("column") }}
```

These methods can also be used in templates to access the blocks.
