# Positional-Only Arguments with Bare `/` in Python

Python 3.8 introduced the `/` marker in function signatures (PEP 570). Every parameter **before** the `/` must be passed positionally — keyword arguments are not allowed for them.

It is the exact opposite of `*` (keyword-only arguments).

## Syntax

```python
def process(user, signed_transaction, /):
    ...
```

## Example

```python
def greet(name, /):
    print(f"Hello {name}")

greet("Alice")          # ✅ works
greet(name="Alice")     # ❌ TypeError: got an unexpected keyword argument
```

## Why This Matters

### 1. Safe parameter renaming

If a parameter isn't positional-only, renaming it is a breaking change for any caller using keyword syntax:

```python
# Without /: renaming 'name' to 'full_name' breaks greet(name="Alice") callers
def greet(name): ...

# With /: callers can't use the name at all, so renaming is safe
def greet(name, /): ...
```

### 2. Matches Python builtins

Many builtins behave this way — `len(obj)`, `abs(x)`, `isinstance(obj, type)`. The `/` lets you document and enforce this explicitly in your own code.

## All Three Zones Together

```python
def func(positional_only, /, normal, *, keyword_only):
    ...

func(1, 2, keyword_only=3)        # ✅
func(1, normal=2, keyword_only=3) # ✅
func(positional_only=1, ...)      # ❌ TypeError
func(1, 2, 3)                     # ❌ TypeError (keyword_only requires a name)
```

| Zone                | Delimiter | Rule            |
| ------------------- | --------- | --------------- |
| Before `/`          | `/`       | Positional only |
| Between `/` and `*` | —         | Either way      |
| After `*`           | `*`       | Keyword only    |

## When to Use

- Library/API code where you want to freely rename parameters without breaking callers.
- Mimicking the behaviour of C-implemented builtins.
- Preventing callers from relying on parameter names as part of your public API.
