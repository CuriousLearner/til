# Keyword-Only Arguments with Bare `*` in Python

Python allows you to force callers to use keyword arguments by placing a bare `*` in the function signature. Every parameter **after** the `*` must be passed by name — positional arguments are not allowed.

## Syntax

```python
def process_subscription(*, user, signed_transaction: str) -> None:
    ...
```

## Example

```python
def process_subscription(*, user, signed_transaction: str) -> None:
    print(f"Processing for {user} with tx: {signed_transaction}")

# Correct — all args passed by keyword
process_subscription(user=alice, signed_transaction="abc123")

# TypeError — positional args not allowed after bare *
process_subscription(alice, "abc123")
```

## Why This Matters

Without `*`, callers can pass arguments positionally, which makes the call site fragile:

```python
# Without *: order matters, easy to mix up
def process_subscription(user, signed_transaction: str) -> None:
    ...

process_subscription(alice, "abc123")       # works, but brittle
process_subscription("abc123", alice)       # silently wrong
```

With `*`, the call site is self-documenting and order-independent:

```python
process_subscription(signed_transaction="abc123", user=alice)  # fine
process_subscription(user=alice, signed_transaction="abc123")  # also fine
```

## Combining with Positional Args

You can mix regular positional args before the `*` and keyword-only args after:

```python
def create_user(username, /, *, role: str, active: bool = True):
    #            ^positional-only  ^keyword-only
    ...

create_user("alice", role="admin")
```

## When to Use

- Functions with many parameters where argument order is easy to confuse.
- Public APIs or signals/tasks where you want to enforce explicitness.
- Any function where swapping two args of the same type would be a silent bug.
