# Using `getent passwd` to query user accounts

`getent passwd` queries the Name Service Switch (NSS) databases for user account information. Unlike directly reading `/etc/passwd`, it includes users from all configured sources (local files, LDAP, NIS, etc.).

## Basic usage

```bash
# List all users
getent passwd

# Query specific user
getent passwd sanyam
```

## Output format

Each line contains 7 colon-separated fields:

```
username:password:UID:GID:GECOS:home_directory:shell
```

Example output:

```
sanyam:x:1000:1000:Sanyam Khurana:/home/sanyam:/bin/bash
```

| Field          | Value            | Description                                         |
| -------------- | ---------------- | --------------------------------------------------- |
| username       | `sanyam`         | Login name                                          |
| password       | `x`              | Password placeholder (actual hash in `/etc/shadow`) |
| UID            | `1000`           | User ID                                             |
| GID            | `1000`           | Primary group ID                                    |
| GECOS          | `Sanyam Khurana` | Full name/comment field                             |
| home_directory | `/home/sanyam`   | User's home directory                               |
| shell          | `/bin/bash`      | Default login shell                                 |

## Why use `getent` over `cat /etc/passwd`

```bash
# Only shows local users
cat /etc/passwd

# Shows ALL users (local + LDAP + NIS + other NSS sources)
getent passwd
```

This distinction matters in enterprise environments where users may be centrally managed.
