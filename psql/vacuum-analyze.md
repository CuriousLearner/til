# VACUUM ANALYZE in PostgreSQL

PostgreSQL uses `VACUUM ANALYZE` to maintain database health and update query planner statistics.

## What it does

**VACUUM**: Reclaims storage occupied by dead tuples (deleted/updated rows)
- Prevents transaction ID wraparound
- Makes space available for reuse (doesn't return it to OS by default)
- Required for bloated tables

**ANALYZE**: Updates statistics used by the query planner
- Collects data about value distributions
- Helps planner choose optimal query execution plans
- Critical for good query performance

## Basic usage

```sql
-- Analyze all tables in current database
VACUUM ANALYZE;

-- Analyze specific table
VACUUM ANALYZE table_name;

-- Just analyze without vacuum
ANALYZE table_name;

-- Verbose output
VACUUM ANALYZE VERBOSE table_name;
```

## When to use

### Run VACUUM ANALYZE when:
- After bulk INSERT/UPDATE/DELETE operations
- Query performance degrades unexpectedly
- `EXPLAIN ANALYZE` shows large discrepancies between estimated and actual rows
- After schema changes or index creation

### Run VACUUM FULL when:
```sql
-- Reclaim disk space (locks table, rewrites entire table)
VACUUM FULL table_name;
```
**Warning**: `VACUUM FULL` locks the table and can take a long time. Use sparingly.

## Auto-vacuum

PostgreSQL runs auto-vacuum in the background by default, but you may need manual runs:

```sql
-- Check auto-vacuum settings
SHOW autovacuum;

-- Check last auto-vacuum/analyze time
SELECT schemaname, relname, last_vacuum, last_autovacuum,
       last_analyze, last_autoanalyze
FROM pg_stat_user_tables
WHERE relname = 'table_name';
```

## Identifying tables that need attention

```sql
-- Tables with most dead tuples
SELECT schemaname, relname, n_dead_tup, n_live_tup,
       round(n_dead_tup * 100.0 / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_pct
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY n_dead_tup DESC
LIMIT 10;

-- Tables not analyzed recently
SELECT schemaname, relname, last_analyze, last_autoanalyze
FROM pg_stat_user_tables
WHERE last_analyze IS NULL OR last_analyze < NOW() - INTERVAL '7 days'
ORDER BY last_analyze NULLS FIRST;
```

## Django integration

```python
from django.db import connection

# Run VACUUM ANALYZE from Django
with connection.cursor() as cursor:
    cursor.execute("VACUUM ANALYZE myapp_mymodel;")
```

## Best practices

1. **Let auto-vacuum handle routine maintenance** for most cases
2. **Manually run after bulk operations** (large imports, migrations)
3. **Monitor statistics age** - stale stats lead to poor query plans
4. **Use VACUUM ANALYZE, not VACUUM FULL** unless you need to reclaim disk space
5. **Schedule during low-traffic periods** for large tables
6. **Check dead tuple ratios** regularly to spot issues early
