## Task 5: Docker Health Checks

Implement a custom health check for a long-running service.

1. Create a Dockerfile for a simple web server (e.g., using `python:alpine` and the built-in `http.server` module)
2. Add a HEALTHCHECK instruction to the Dockerfile
3. Build and run the container
4. Use `docker inspect` to view the health status

docker build -t healthcheck .
docker run -d --name python_server -p 8000:8000 healthcheck
docker inspect --format='{{json .State.Health}}' python_server
docker inspect --format='{{.State.Health.Status}}' python_server
