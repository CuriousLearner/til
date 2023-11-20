# Filter list of docker containers

`docker ps` commands offer `-q` stands for `quiet`, that only displays container ids.

The `-f` flag is for filtering the list of running containers based on conditions provided.

For example:

```
docker ps -qf "name=django-web"
```

will list down the container id for container with name as `django-web`.

You may plug it into commands like:

```
docker exec -it $(docker ps -qf "name=django-web") python manage.py migrate
```

to run the migrations from the django container.
