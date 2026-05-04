# `df.repartition(N)` in Spark

`repartition(N)` reshuffles the data across the cluster into exactly `N` partitions using a **full shuffle**.

## Basic Usage

```python
df = df.repartition(10)       # reshuffle into 10 partitions
df = df.repartition(10, "id") # reshuffle into 10 partitions, hash-partitioned by 'id'
```

## Why It Matters

Spark processes each partition in parallel. Too few partitions → underutilized cluster. Too many → scheduling overhead dominates.

```python
df.rdd.getNumPartitions()  # check current partition count
```

## `repartition` vs `coalesce`

|                     | `repartition(N)`              | `coalesce(N)`                            |
| ------------------- | ----------------------------- | ---------------------------------------- |
| Shuffle             | Full shuffle                  | Avoids shuffle (merges local partitions) |
| Increase partitions | ✅                            | ❌ (can only decrease)                   |
| Even distribution   | ✅                            | ❌ (can produce skewed partitions)       |
| Use when            | Increasing OR need even split | Decreasing, e.g. before writing output   |

```python
# Writing output — reduce partitions cheaply before save
df.coalesce(1).write.parquet("output/")

# After a big filter that left data skewed — re-balance
df.filter(df.status == "active").repartition(50)
```

## Common Rule of Thumb

- Target **~128 MB per partition** as a starting point.
- Default shuffle partitions in Spark is `200` (`spark.sql.shuffle.partitions`). Tune this for your data size:

```python
spark.conf.set("spark.sql.shuffle.partitions", "50")
```

## Pandas Equivalent

Pandas itself is single-node and has no `repartition`. The concept applies in:

- **PySpark pandas API** (`pyspark.pandas`): same `df.spark.repartition(N)` under the hood.
- **Dask**: `df.repartition(npartitions=N)` — similar idea, splits/merges partitions across workers.
