# Speed Up Django Admin with `list_select_related`

Django Admin can get **slow** when displaying related fields due to multiple database queries. Use `list_select_related` to **optimize performance** by fetching related data in a **single query**.

## Example

You have an `Order` model with a foreign key to `Customer`:

```python
class Order(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
```

In Django Admin:

```python
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "total_price")
    list_select_related = ("customer",)  # Pre-fetch related customer data in one query
```

## Why?
🔹 **Without `list_select_related`** → Each row triggers an **extra query** for `customer`.
🔹 **With `list_select_related`** → Uses **JOINs** to fetch all related data **at once**, reducing query count.

💡 **Pro Tip:** For **multiple ForeignKeys**, use `list_select_related = ("customer", "sales_rep")`.
🚀 **Result:** Faster Django Admin with fewer queries!
