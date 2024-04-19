# Use text objects to make efficient changes

If you want to change something enclosed within brackets, curly braces, quotes, you can use:

- `ci(` – **C**hange **I**nside brackets
 for changing

```python
my_func(something)
```

to

```python
my_func(something_else)
```

- `da”` – **D**elete **A**round double quotes

```python
print("Hello, World!")
```

to

```python
print()
```

- `di]` – **D**elete **I**nside square brackets

```python
my_list = [1, 2, 3]
```

to

```python
my_list = []
```

- `ci{` – **C**hange **I**nside curly braces

```python
my_dict = {"key": "value"}
```

to

```python
my_dict = {"key": "new_value"}
```


- `dap` – **D**elete **A**round **P**aragraph

```python
def my_func():
    print("Hello, World!")
```

to

```python
```

- `ciw` – **C**hange **I**nside **W**ord

```python
my_var = "value"
```

to

```python
my_var = "new_value"
```



- `vaw` – **V**isually select **A**round **W**ord

```python
my_var = "value"
```

to

```python
my_var = "new_value"
```
