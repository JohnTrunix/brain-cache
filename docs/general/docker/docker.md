# Docker :simple-docker:

Docker is a containerization platform that allows you to run applications in a sandboxed environment. This means that you can run applications in a container without having to worry about the dependencies and libraries that the application needs to run.

## Concept

Docker builds images from a `Dockerfile` and runs containers from an image. The Docker technology uses the Linux kernel features such as namespaces and control groups to create containers on top of an operating system. [^1]

All Docker Images are made up of a series of layers which are are combined together. Each command such as `RUN`, `COPY`, `ADD`, etc. in the `Dockerfile` creates a new layer. When you change a `Dockerfile` and rebuild the image, only the layers that have changed are rebuilt. This is called **layer caching**. This accelerates the building process.

## Most used commands

### Pull Docker Image

Pulls an image from a registry.

```bash
docker pull <image>
```

### List running Containers

Lists all running containers.

```bash
docker ps
```

### Exec command in Container

Executes a command in a running container with a shell.

```bash
docker exec -it <container> \bin\bash
```

-   `-i` flag is used for interactive mode
-   `-t` flag is used to enable terminal typing

Executes a command in a running container without a shell.

```bash
docker exec -it <container> <command>
```

### Build Docker Image

Builds an image from a `Dockerfile`.

```bash
docker build .
```

-   `.` is the root of the project (build context)

-   `-f` flag is used to specify an alternative `Dockerfile`:

    ```bash
    docker build -f Dockerfile.dev .
    ```

-   `-t` flag is used to tag the image with a name:

    ```bash
    docker build -t myimage .
    ```

### Run Docker Container

Runs a container from an image. [^2]

```bash
docker run <image>
```

-   `<image>` can be identified by the tagname or the image id
-   `-d` flag is used to run the container in detached mode
-   `-rm` flag is used to remove the container after it exits
-   `-p <host-port>:<container-port>` flag is used to publish a container's port to the host
-   `-v <host-path>:<container-path>` flag is used to mount a volume from the host to the container (manually)

## Dockerfile

General format of a `Dockerfile`[^3]:

```dockerfile
INSTRUCTION arguments
```

### Example

```dockerfile
ARG version=3.8
FROM python:$version
LABEL version="1.0.0"
LABEL about="This is a sample Dockerfile"
ENV output "Hello Docker 🐋!"
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["echo", "$output"]
```

```bash
docker build -t myimage .
docker run myimage
```

### Comments

```dockerfile
# This is a comment
```

### `ARG`

Defines a variable that is used in the build-tiem. It is also the only way to pass arguments to a `FROM` instruction.

```dockerfile
ARG version=3.8
FROM python:$version
```

### `FROM`

Define the base image for the container. This is the image that will be used to build the container and other layers on top of it.

```dockerfile
FROM python:3.8
```

### `LABEL`

Adds metadata to an image.

```dockerfile
LABEL version="1.0.0"
LABEL about="This is a sample Dockerfile"
```

### `ENV`

Sets an environment variable for all commands that follow it in the `Dockerfile`. This is **not used** for building instructions of the image, instead it is used for **running instructions for the image**.

```dockerfile
ENV output "Hello Docker 🐋!"
CMD ["echo", "$output"]
```

### `WORKDIR`

Sets the working directory for all commands that follow it in the `Dockerfile`.

```dockerfile
WORKDIR /app
```

!!! note

    You can use `WORKDIR` multiple times in a `Dockerfile`. Each time it is used, it will change the working directory for all commands that follows.

### `COPY`

Copies files from the host machine to the container.

```dockerfile
COPY requirements.txt .
```

### `ADD`

Copies files from the host machine to the container. It can also download files from the internet and extract compressed files.

```dockerfile
ADD requirements.txt .
ADD https://example.com/file.zip .
```

### `VOLUME`

Creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers.

```dockerfile
VOLUME /data
```

### `EXPOSE`

Is used as documentation to specify which ports the container listens on.

```dockerfile
EXPOSE 80 443
```

!!! note

    It does not actually publish the port. To publish the port, you must use the `-p` flag with the `docker run` command:

    ```bash
    docker run -p 80:80 -p 443:443 <image>
    ```

### `USER`

Sets the user name or UID to use when running the image. This is useful when you want to run the container as a non-root or a specific user.

```dockerfile
USER myuser
CMD ["whoami"]
```

### `RUN`, `CMD` and `ENTRYPOINT`

#### `CMD`

Define the command that will be executed as default when no other arguments are passed to the `docker run` command. This is used for **running instructions in the image**.

```dockerfile
CMD ["echo", "Hello Docker 🐋!"]
```

!!! note

    - `docker run ls -la` will execute `ls -la` command inside the container instead of the `CMD` command.
    - only the last `CMD` instruction will be executed.

#### `ENTRYPOINT`

Define the default command that will be executed when the container is started and adds arguments passed from the `docker run` command or `CMD` instruction. This is used for **running instructions in the image**.

```dockerfile
CMD ["Hello Docker 🐋!"]
ENTRYPOINT ["echo"]
```

#### `RUN`

Executes a command in the container in a new layer on top of the current image and commits the results for the next commands. This is used for **building instructions for the image** and will be saved in the image.

```dockerfile
RUN pip install -r requirements.txt
```

!!! note

    When using `USER` instruction, you must make sure that the user exists in the image. While using UID the user does not need to exist.

#### Example

You want to run a container for `dev` and `prod` environments. The only differences are:

-   `dev` environment should run the application with hot-reload enabled: `--reload`
-   `prod` environment should run the application with an production flag: `--prod`

```dockerfile
FROM python:3.8
ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--prod"]
```

Running `dev` environment with hot-reload enabled (this overrides the `CMD` instruction):

```bash
docker run myimage --reload
```

Running `prod` environment with production flag enabled (this uses the `CMD` instruction):

```bash
docker run myimage
```

## .dockerignore

When building the image at the root level, Docker sends entire context to the Docker deamon. This can cause the build to fail if there are files that should not be sent to the deamon.

To avoid this, you can create a `.dockerignore` file in the root of the project and add the files that should not be sent to the deamon.

```text
.git
env
```

[^1]: [https://www.redhat.com/en/topics/containers/what-is-docker](https://www.redhat.com/en/topics/containers/what-is-docker){target=\_blank}
[^2]: [https://docs.docker.com/engine/reference/commandline/container_run/](https://docs.docker.com/engine/reference/commandline/container_run/){target=\_blank}
[^3]: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/){target=\_blank}
