# `envsubst` command for substituting values in config files

We can have files that contain variables which are replaced by environment variables at runtime. This is particularly useful for configuration files, where sensitive information like API keys or database passwords should not be hardcoded and checked into version control.

`envsubst` is a command-line utility used for substituting the values of environment variables into strings or files. It's particularly useful for templating configuration files with environment-specific values.

## Example:

Suppose you have a configuration template file `config.template` with the following content:

```bash
api_url=http://$API_HOST:$API_PORT/api
db_url=postgres://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME
```

Define env variables:

```bash
export API_HOST=api.example.com
export API_PORT=8080
export DB_USER=myuser
export DB_PASS=mypassword
export DB_HOST=db.example.com
export DB_PORT=5432
export DB_NAME=mydatabase
```

Run `envsubst` to replace the placeholders with the actual values:

```bash
envsubst < config.template > config.conf
```

This will create a new file `config.conf` with the environment variables replaced.

The `config.conf` will now look like this:

```bash
api_url=http://api.example.com:8080/api
db_url=postgres://myuser:mypassword@db.example.com:5432/mydatabase
```
