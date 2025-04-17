# Project Setup and Management

This project uses Docker and Docker Compose to manage the development environment. The `Makefile` provides a set of commands to build, start, stop, and manage the Docker containers.

It's designed to be used with a Python application and includes a MySQL database (MariaDB) and RabbitMQ for message queuing.

## Prerequisites

- Docker
- Docker Compose
- Make
- awk
- gawk

## Commands

### `make all`

This command is a placeholder and does not perform any actions. It is included for completeness.

### `make pre-up`

Displays the current user ID, group ID, and target architecture.

### `make build`

Builds the Docker images with the appropriate architecture.

### `make up`

Runs the `pre-up` and `build` commands, then starts the Docker containers in detached mode.

### `make down`

Stops and removes the Docker containers, volumes, and images.

### `make stop`

Stops the Docker containers without removing them.

### `make status`

Displays the status of the Docker containers.

### `make setup`

Starts the Docker containers, Builds the images with the appropriate architecture, and installs Composer dependencies.

## Usage

1. **Build and start the containers:**

   ```sh
   make up
    ```
   
2. **Stop and remove the containers, volumes, and images:**

    ```sh
    make down
    ```
   
3. **Stop the containers without removing them:**

    ```sh
    make stop
    ```
   
4. **Display the status of the containers:**

    ```sh
    make status
    ```
   
5. **Set up the project:**

    ```sh
    make setup
    ```
   
6. **Display the current user ID, group ID, and target architecture:**

    ```sh
    make pre-up
    ```
   
7. **Build the Docker images:**

    ```sh
    make build
    ```

## RabbitMQ

The RabbitMQ service is included in the Docker Compose file. It is used for message queuing and can be configured as needed.

## Python

The Python application is set up to use the `python:3.11` slim image.

## Python (consumer)

The Python consumer is set up to use the `python:3.11` slim image.
It is designed to consume messages from RabbitMQ and process them.\
The consumer is set up to run in a separate container and can be configured as needed.\
The `docker-compose.yml` file defines the service, and the `Dockerfile` is used to build the image.   

Launch is delayed to ensure that the RabbitMQ service is up and running before the consumer container starts (using healthcheck status).

## MySQL

The MySQL service is set up to use the `mariadb:latest` image.

## DB Autoload

The `db` directory is used to load the database schema and data when the MySQL container is started.

- The `.sql` file is used to create the database schema.

## Docker Compose

The `docker-compose.yml` file defines the services, networks, and volumes used in the project.

Can be used to start the application and database containers + rabbitmq (can be commented or adapted to other messaging queues if needed).

## Dockerfile

The `Dockerfile` is used to build the Docker images for the application. It includes the following steps:
- Set the base image to `python:3.11-slim`.
- Install required packages.

Provided requirements.txt file is only as a placeholder, you can adapt it to your needs.

## Notes

- `src` folder contains basic example files which are only here to illustrate the usage of the Docker setup.
- Ensure that Docker and Docker Compose are installed and running on your system.
- The `CURRENT_UID` and `CURRENT_GID` environment variables are used to set the file ownership inside the Docker containers to match the host user.