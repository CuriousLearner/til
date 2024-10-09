# YAML Anchor Tags using `<<:` and `*` Syntax

YAML anchors help avoid repetition by allowing reuse of values using `&` (to define), `*` (to reference), and `<<:` (to merge).

### Example with `*` Syntax

```yaml
base: &default-settings
  timeout: 30
  retries: 5

service1:
  settings: *default-settings
  url: "http://service1.com"

service2:
  settings: *default-settings
  url: "http://service2.com"
  retries: 3  # Override retries for service2
```

### Example with `<<:` for Merging

```yaml
defaults: &defaults
  timeout: 10
  retries: 3

overrides: &overrides
  timeout: 20

combined:
  <<: [*defaults, *overrides]
  url: "http://example.com"
```

## Key Points

- `*` References an anchor.
- `<<:` Merges values from one or more anchors.
- Anchors reduce duplication and simplify YAML configuration.
