# Managing Schema-less Migrations in Django with `SeparateDatabaseAndState`

Ever needed to update Django’s ORM model without altering the actual database schema? That’s where `SeparateDatabaseAndState` comes in.

## Use Case

Imagine you’re working with an **external read-only reporting database** (`legacy_db`) where Django should track relationships but **shouldn’t modify tables**. You have:

```python
class Order(models.Model):
    legacy_customer = models.CharField(max_length=255, db_column="customer_id")
```

Now, you want to change this field into a `ForeignKey` to `LegacyCustomer` without actually modifying `legacy_db.customer`:

```python
class Order(models.Model):
    legacy_customer = models.ForeignKey(
        "legacy.LegacyCustomer",
        to_field="customer_id",
        db_column="customer_id",
        on_delete=models.DO_NOTHING,
        db_constraint=False,
    )
```

Applying this as a standard migration could fail or modify `legacy_db`, which we don’t want. Instead, use:

```python
migrations.SeparateDatabaseAndState(
    state_operations=[
        migrations.RemoveField("order", "legacy_customer"),
        migrations.AddField(
            "order",
            "legacy_customer",
            models.ForeignKey(
                "legacy.LegacyCustomer",
                to_field="customer_id",
                db_column="customer_id",
                on_delete=models.DO_NOTHING,
                db_constraint=False,
            ),
        ),
    ]
)
```

This updates Django’s ORM state **without touching the external DB**. 🚀
