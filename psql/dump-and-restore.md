# Dump and Restore database

To dump:

```bash
PGPASSWORD=<password> pg_dump --username <username> <dbname> > dump.sql
```

To restore:

```bash
PGPASSWORD=<password> psql --username <username> <dbname> -p <port> -h <host> < dump.sql
```
