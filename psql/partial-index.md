# Partial Index

A partial index in PostgreSQL is an index built over a subset of rows in a table, defined by a `WHERE` clause. This makes the index smaller, faster to scan, and cheaper to maintain compared to a full index.

## Syntax

```sql
CREATE INDEX index_name ON table_name (column_name)
WHERE condition;
```

## Example

Consider an `orders` table where most queries filter for active (unshipped) orders, but the vast majority of rows are already shipped:

```sql
CREATE INDEX idx_orders_pending ON orders (created_at)
WHERE status != 'shipped';
```

This index only includes rows where `status != 'shipped'`, so it stays small even as the table grows with millions of shipped orders.

## When to use partial indexes

- **Skewed data distributions** — when queries target a small subset of rows (e.g., `WHERE active = true` on a table that's 95% inactive)
- **Soft deletes** — index only non-deleted rows: `WHERE deleted_at IS NULL`
- **Status-based filtering** — index only rows in a specific state: `WHERE status = 'pending'`
- **Unique constraints on a subset** — enforce uniqueness only where it matters:

```sql
CREATE UNIQUE INDEX idx_unique_active_email ON users (email)
WHERE deleted_at IS NULL;
```

This allows multiple rows with the same email as long as only one is non-deleted.

## Verifying the index is used

Use `EXPLAIN ANALYZE` to confirm PostgreSQL uses the partial index:

```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE status != 'shipped' AND created_at > '2025-01-01';
```

Look for `Index Scan using idx_orders_pending` in the output. If the query's `WHERE` clause doesn't imply the index's predicate, PostgreSQL won't use it.

## Important notes

- The query's `WHERE` clause must logically match or imply the index's condition for the planner to consider it.
- Partial indexes reduce index size and write amplification since inserts/updates to rows outside the predicate don't touch the index at all.
- They can be combined with any index type (`btree`, `gin`, `gist`, etc.).
