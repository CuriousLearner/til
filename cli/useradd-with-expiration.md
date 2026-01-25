# Creating user accounts with expiration dates

Use `useradd -e` to create accounts that automatically expire on a specific date. Useful for temporary contractors, interns, or time-limited access.

## Create user with expiration

```bash
sudo useradd -m -e 2027-03-28 rose
```

| Flag | Description |
| ---- | ----------- |
| `-m` | Create home directory |
| `-e` | Account expiration date (YYYY-MM-DD format) |

## Verify expiration date

```bash
sudo chage -l rose | grep -i "Account expires"
# Output: Account expires : Mar 28, 2027
```

Or view all account aging info:

```bash
sudo chage -l rose
```

## Modify expiration on existing user

```bash
# Change expiration date
sudo chage -E 2027-06-30 rose

# Remove expiration (never expires)
sudo chage -E -1 rose
```

## Related: password expiration vs account expiration

- **Account expiration** (`-e`/`-E`): User cannot log in at all after this date
- **Password expiration** (`-M`): User must change password after N days, but can still log in
