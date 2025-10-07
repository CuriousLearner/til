# Override Migration Locations with MIGRATION_MODULES in Django

Django's `MIGRATION_MODULES` setting allows you to override the default location where migrations are stored for specific apps. This is particularly useful when you need to extend or modify migrations for third-party packages without touching their source code in site-packages.

```python
# settings.py
MIGRATION_MODULES = {
    'myapp': 'myproject.db.migrations.myapp',
    'third_party_app': 'myproject.db.migrations.third_party_app',
}
```

## Common use cases

### 1. Extend third-party package migrations

When you need to add custom migrations to third-party packages (e.g., to modify field constraints):

```python
MIGRATION_MODULES = {
    # Redirect easy_thumbnails migrations to our controlled directory
    # This allows us to extend/modify them without touching site-packages
    "easy_thumbnails": "myproject.apps.core.easy_thumbnails_migrations",
}
```

**Real-world example**: Increasing field length limits when the default constraints are too restrictive:

```python
# In your custom migration file
# myproject/apps/core/easy_thumbnails_migrations/0003_increase_name_length.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('easy_thumbnails', '0002_previous_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='name',
            field=models.CharField(max_length=500),  # Increased from 255
        ),
    ]
```

This approach is preferable when alternatives would be disruptive:
- Changing thumbnail naming strategy would regenerate all existing thumbnails (wasteful at scale)
- Modifying site-packages is fragile and lost on updates

### 2. Disable migrations for an app

Set the migration location to `None` to completely disable migrations for an app (useful in testing):

```python
MIGRATION_MODULES = {
    'third_party_app': None,
}
```

### 3. Centralize migrations

Keep all migrations in a central location for better organization:

```python
MIGRATION_MODULES = {
    'auth': 'myproject.migrations.auth',
    'contenttypes': 'myproject.migrations.contenttypes',
    'sessions': 'myproject.migrations.sessions',
}
```

## Important considerations

**Testing**: When `MIGRATION_MODULES` is set to `None` for an app, Django will create the tables from scratch using the current models without running migrations. This can speed up tests but may miss migration-related issues.

**Deployment**: Ensure the custom migration directories exist and are included in your version control. Django will create migration files in the specified location when you run `makemigrations`.

**Path structure**: The migration module path must be a valid Python import path. Create the necessary directory structure and `__init__.py` files.

```bash
# Example structure for custom migration location
myproject/
├── migrations/
│   ├── __init__.py
│   ├── auth/
│   │   └── __init__.py
│   └── third_party_app/
│       └── __init__.py
```

Use `MIGRATION_MODULES` when you need fine-grained control over where Django stores and looks for migrations, especially when working with third-party packages or optimizing test performance.
