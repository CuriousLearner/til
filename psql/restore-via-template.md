# Restore database via template

To restore a PostgreSQL database using a template, you can use the `createdb` command with the `--template` option. This method is faster than traditional backup and restore because it copies the database files directly, avoiding the overhead of SQL-based operations.

For PostgreSQL 15, the createdb command uses the `WAL_LOG` method by default. This method copies the database block by block and logs each block in the write-ahead log. It's the most efficient strategy for small template databases.

The older `FILE_COPY` method writes a small record to the write-ahead log for each tablespace, representing a directory copy at the filesystem level.

Example:

To create a new database `newdb` from the template `templatedb`:

```bash
createdb newdb --template=templatedb
```

This command efficiently copies the schema and data from `templatedb` to `newdb`.

With create database command,

```sql
create database newdb template templatedb;
```
