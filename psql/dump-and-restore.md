# Dump and Restore database

To dump:

```
PGPASSWORD=<password> pg_dump --username <username> <dbname> > dump.sql
```

To restore:

```
PGPASSWORD=<password> psql --username <username> <dbname> -p <port> -h <host> < dump.sql
```
