# Get rid of persistent volumes in `docker compose down`

```bash
docker compose down -v db
```

`docker-compose down`: This command stops and removes the containers, networks, volumes, and other resources created by `docker-compose up`. It is a convenient way to clean up resources after running Docker Compose services.

`-v db`: The `-v` option instructs Docker Compose to remove the volume associated with the specified service (`db` in this case). This ensures that not only containers but also any persistent data stored in the volume is deleted. Useful when you want to clean up the entire database service, including its associated data volume, without affecting other services defined in the `docker-compose.yml`.
