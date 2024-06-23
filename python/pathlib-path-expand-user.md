# Expand home directory paths in `pathlib.Path`

To expand home directory paths in `pathlib.Path`, use the `expanduser()` method. This converts the `~` to the full home directory path.

```python
from pathlib import Path

path = Path("~/.private_keys/project-x.2024-06-23.private-key.pem").expanduser()

# Users/CuriousLearner/.private_keys/project-x.2024-06-23.private-key.pem
```
