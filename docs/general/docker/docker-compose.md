# Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. Information describing the services and networks for an application are contained within a YAML file, called docker-compose.yml. [^1]

## Elements `docker-compose.yml`

-   [Version](https://docs.docker.com/compose/compose-file/compose-versioning/)
-   [Services](https://docs.docker.com/compose/compose-file/05-services/)
-   [Networks](https://docs.docker.com/compose/compose-file/06-networks/)
-   [Volumes](https://docs.docker.com/compose/compose-file/07-volumes/)
-   [Configurations](https://docs.docker.com/compose/compose-file/08-configs/)
-   [Secrets](https://docs.docker.com/compose/compose-file/09-secrets/)

## File Structure

```yaml
version: "x.x"

services:
    <service-name-1>:
        build: <path-to-dockerfile>
        ports:
            - "<host-port>:<container-port>"
        volumes:
            - "<host-path>:<container-path>"
        networks:
            - <network-name-1>

    <service-name-2>:
        image: <image-name>
        ports:
            - "<host-port>:<container-port>"
        volumes:
            - "<host-path>:<container-path>"
        depends_on:
            - <service-name-1>
        networks:
            - <network-name-1>
            - <network-name-2>

    <database-service-name>:
        image: <image-name>
        ports:
            - "<host-port>:<container-port>"
        volumes:
            - "<host-path>:<container-path>"
        environment:
            - POSTGRES_USER=<username>
            - POSTGRES_PASSWORD=<password>
            - POSTGRES_DB=<database-name>
        networks:
            - <network-name-2>

networks:
    <network-name-1>:
    <network-name-2>:
```

## Commands

### Build

This command builds/rebuilds the images for the services defined in the `docker-compose.yml` file.

```bash
docker-compose build
```

### Run

Similar to `docker run`, this command runs the containers for the services defined in the `docker-compose.yml` file.

```bash
docker-compose run
```

### List

This command lists all containers for the services defined in the `docker-compose.yml` file.

```bash
docker-compose ps
```

### Up

This command builds and runs the containers for the services defined in the `docker-compose.yml` file.

```bash
docker-compose up
```

### Down

This command stops the containers for the services defined in the `docker-compose.yml` file.

```bash
docker-compose down
```

[^1]:
    [https://www.educative.io/blog/docker-compose-tutorial](https://www.educative.io/blog/docker-compose-tutorial)
    c
