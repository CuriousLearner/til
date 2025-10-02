# Using EXPLAIN and EXPLAIN ANALYZE for Django QuerySets

Django provides `.explain()` to analyze query execution plans and identify performance bottlenecks.

## Basic usage

```python
# EXPLAIN - Shows query plan without execution
print(Article.objects.filter(status='published').explain())

# EXPLAIN ANALYZE - Actually runs the query and shows real timing
print(Article.objects.filter(status='published').explain(analyze=True))
```

## Reading the results

The output varies by database, but here's what to look for in PostgreSQL:

```
Seq Scan on article  (cost=0.00..35.50 rows=10 width=100) (actual time=0.012..0.156 rows=8 loops=1)
  Filter: (status = 'published'::text)
  Rows Removed by Filter: 2
Planning Time: 0.084 ms
Execution Time: 0.198 ms
```

### Key metrics

**cost=0.00..35.50**: Estimated startup cost..total cost (arbitrary units)
- Lower is better
- Used by query planner to choose between strategies

**rows=10**: Estimated number of rows returned

**actual time=0.012..0.156**: Real startup time..total time in milliseconds (only with `analyze=True`)

**rows=8**: Actual rows returned (only with `analyze=True`)

**Planning Time / Execution Time**: Total time breakdown

## Identifying bottlenecks

### Sequential scans on large tables
```
Seq Scan on article  (cost=0.00..10000.00 rows=500000 width=100)
```
**Problem**: Full table scan instead of using an index
**Solution**: Add an index on the filtered column

### Missing index usage
```python
# Check if an index is being used
print(Article.objects.filter(created_at__gte=date).explain())
# Look for "Index Scan" or "Index Only Scan" instead of "Seq Scan"
```

### Nested loops on large datasets
```
Nested Loop  (cost=0.00..50000.00 rows=10000 width=200)
```
**Problem**: Inefficient join strategy
**Solution**: Use `select_related()` or check if statistics are outdated (run `ANALYZE` on tables)

### High actual vs estimated rows
```
Hash Join  (cost=10.00..20.00 rows=100 width=50) (actual rows=50000 loops=1)
```
**Problem**: Query planner has outdated statistics
**Solution**: Run `VACUUM ANALYZE` on the table

## Database-specific options

```python
# PostgreSQL: verbose output with buffer usage
Article.objects.all().explain(verbose=True, analyze=True, buffers=True)

# PostgreSQL: different output formats
Article.objects.all().explain(format='json', analyze=True)
```

## Best practices

1. **Always use `analyze=True` for real performance data** - estimated costs can be misleading
2. **Test with production-like data volumes** - query plans change with table size
3. **Look for sequential scans** on large tables first - usually the biggest wins
4. **Check actual time** at each node to find the slowest operation
5. **Compare estimated vs actual rows** - large differences indicate stale statistics
