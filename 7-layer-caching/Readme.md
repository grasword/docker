## Task 7: Docker Layer Caching and Optimization

Optimize a Dockerfile to make effective use of layer caching.

1. Create a Dockerfile that installs multiple packages and copies multiple files
2. Build the image and note the build time
3. Modify the Dockerfile to optimize layer caching (e.g., combine RUN instructions, order instructions effectively)
4. Rebuild and compare build times

time docker build -t myapp:initial .

time docker build -t myapp:optimized .
