# Autouse fixtures for common test dependencies

Fixtures can be marked as autouse, meaning they will be invoked for all tests in a module without a direct dependency on them. This can be useful for setting up common test dependencies, such as a temporary directory or a database connection.

```python
import pytest

@pytest.fixture(autouse=True)
def setup_database():
    print("\nSetup database")
    yield
    print("\nTeardown database")

def test_insert_data():
    print("Inserting data")

def test_delete_data():
    print("Deleting data")
```

When running the tests, the output will be:

```shell
Setup database
Inserting data
Teardown database
Setup database
Deleting data
Teardown database
```

In the above example, the `setup_database` fixture is marked as autouse, so it will be invoked for all tests in the module. The fixture sets up the database before each test and tears it down after each test.
