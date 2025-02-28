# Print SQL on ORM queries

One way to know what SQL queries are being run on executing an ORM statement is with the following:

```python
from django.db import connection

connection.queries
```

Django Extensions makes it easy to print all SQL queries if you pass an extra parameter while running shell like:

```bash
python manage.py shell_plus --print-sql
```
