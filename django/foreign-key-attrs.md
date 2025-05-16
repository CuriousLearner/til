# Understanding Django ForeignKey Fields

Django’s `ForeignKey` has several useful options that control how relationships behave. Here are some you should know:

```python
class Invoice(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,  # Deletes Invoice if Customer is deleted
        to_field="customer_code",  # Links to a non-PK field
        db_column="customer_id",   # Custom column name in the DB
        related_name="invoices",   # Enables reverse lookup: customer.invoices.all()
        db_constraint=True,        # Enforces FK constraint at the DB level
    )
```

🔹 `on_delete=models.CASCADE` → Deletes invoices when the customer is deleted.
🔹 `to_field="customer_code"` → Uses `customer_code` instead of the default `id`.
🔹 `db_column="customer_id"` → Maps the field to a specific column in SQL.
🔹 `related_name="invoices"` → Allows reverse access like `customer.invoices.all()`.
🔹 `db_constraint=False` → Removes DB-level constraints, useful for external references.

Want a `ForeignKey` without constraints? Set `db_constraint=False`, but be mindful of orphaned records.
