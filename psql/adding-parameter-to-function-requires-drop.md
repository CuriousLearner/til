# Adding a Parameter to a Postgres Function Requires DROP First

Postgres identifies a function by its **name + input argument type list** (the signature). The return type and default values are not part of the identity. This has a sharp consequence when you add a new parameter to an existing function.

## The Problem

Suppose you have:

```sql
CREATE OR REPLACE FUNCTION get_product_price(
    p_product_id   uuid,
    p_currency     varchar,
    p_quantity     integer,
    p_discount     numeric,
    p_metadata     jsonb
) RETURNS TABLE(...) ...
```

And you want to add an optional parameter:

```sql
CREATE OR REPLACE FUNCTION get_product_price(
    p_product_id   uuid,
    p_currency     varchar,
    p_quantity     integer,
    p_discount     numeric,
    p_metadata     jsonb,
    p_region_id    uuid DEFAULT NULL   -- new param
) RETURNS TABLE(...) ...
```

`CREATE OR REPLACE` does **not** replace the 5-arg version. Because the signature changed (5 args → 6 args), Postgres treats this as a brand new function. Both now exist simultaneously.

## Why That Breaks Existing Callers

Any caller that was calling the 5-arg version now matches **two** candidates:

1. The 5-arg function — exact match.
2. The 6-arg function — via the `DEFAULT NULL` on the 6th param.

Postgres cannot prefer one over the other and raises:

```
ERROR: function get_product_price(uuid, character varying, integer, numeric, jsonb) is not unique
```

The existing calling function fails at runtime even though it hasn't changed.

## The Fix: DROP the Old Signature First

```sql
-- Idempotent: no-op on subsequent deploys once the 5-arg version is gone
DROP FUNCTION IF EXISTS get_product_price(uuid, varchar, integer, numeric, jsonb);

CREATE OR REPLACE FUNCTION get_product_price(
    p_product_id   uuid,
    p_currency     varchar,
    p_quantity     integer,
    p_discount     numeric,
    p_metadata     jsonb,
    p_region_id    uuid DEFAULT NULL
) RETURNS TABLE(...) ...
```

With only the 6-arg function present, the existing 5-arg call resolves to it cleanly through the default. No caller changes needed.

## Key Rules

- Postgres function identity = **name + input arg types**. Return type and defaults are irrelevant to identity.
- `CREATE OR REPLACE` only works in-place if the signature (name + arg types) is unchanged.
- Adding any parameter — even one with a `DEFAULT` — creates a new overload, not a replacement.
- `DROP FUNCTION IF EXISTS` with the **old** signature is idempotent and safe to leave in migrations permanently.
