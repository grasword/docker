# docker

# Tasks / Docker

## Task 1: Multi-stage Builds

Create a Dockerfile that uses multi-stage builds to compile a simple C program and create a minimal final image.

1. Create a file named hello.c with a simple "Hello, Docker!" program
2. Create a Dockerfile that:
   - Uses gcc:latest as the build stage
   - Compiles the C program
   - Uses alpine:latest as the final stage
   - Copies only the compiled binary to the final stage
3. Build and run the Docker image

## Task 2: Custom Bridge Network and Container Communication

Create two containers that can communicate over a custom bridge network.

1. Create a custom bridge network
2. Run an Alpine container with a custom name on this network
3. Run another Alpine container on the same network
4. Demonstrate communication between the containers using ping

## Task 3: Volume Mounting and Data Persistence

Use volume mounting to persist data between container runs.

1. Create a Docker volume
2. Run a container that mounts this volume and writes data to it
3. Stop and remove the container
4. Run a new container that mounts the same volume
5. Verify that the data persists

## Task 4: Docker Compose for Multi-Container Setup

Use Docker Compose to set up a multi-container environment.

1. Create a docker-compose.yml file that defines:
   - A Redis service
   - An Alpine service that depends on Redis
2. Use environment variables in the Compose file
3. Define a custom network for the services
4. Use the command option to run a custom command in the Alpine container

## Task 5: Docker Health Checks

Implement a custom health check for a long-running service.

1. Create a Dockerfile for a simple web server (e.g., using python:alpine and the built-in http.server module)
2. Add a HEALTHCHECK instruction to the Dockerfile
3. Build and run the container
4. Use docker inspect to view the health status

## Task 6: Resource Constraints and Load Testing

Run a container with specific resource constraints and perform a load test.

1. Create a Dockerfile for a simple Flask web application that performs a CPU-intensive task (e.g., calculating Fibonacci numbers)
2. Build and run the container with CPU and memory constraints
3. Use Apache Benchmark (ab) to perform a load test on the container
4. Monitor the container's resource usage during the load test using docker stats
5. Analyze the results

## Task 7: Docker Layer Caching and Optimization

Optimize a Dockerfile to make effective use of layer caching.

1. Create a Dockerfile that installs multiple packages and copies multiple files
2. Build the image and note the build time
3. Modify the Dockerfile to optimize layer caching (e.g., combine RUN instructions, order instructions effectively)
4. Rebuild and compare build times

## Task 8: Using Docker Configs for Nginx Configuration

Learn how to use Docker configs to manage and update Nginx configuration without rebuilding containers.

Objective: Understand how to use Docker configs to externalize configuration files, allowing for dynamic updates to running containers without rebuilds.

Use Case: Manage a web server that needs frequent configuration changes. Use Docker configs to update the server configuration without rebuilding or restarting the entire container.

Tasks:

1. Create an initial Nginx configuration file
2. Create a Docker config from this file
3. Run an Nginx container using this config
4. Test the server
5. Create an updated Nginx configuration file
6. Create a new Docker config
7. Update the running container to use the new config
8. Test the server again to see the updated response
