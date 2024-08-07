## Task 1: Multi-stage Builds

Create a Dockerfile that uses multi-stage builds to compile a simple C program and create a minimal final image.

1. Create a file named `hello.c` with a simple "Hello, Docker!" program
2. Create a Dockerfile that:
   - Uses `gcc:latest` as the build stage
   - Compiles the C program
   - Uses `alpine:latest` as the final stage
   - Copies only the compiled binary to the final stage
3. Build and run the Docker image
