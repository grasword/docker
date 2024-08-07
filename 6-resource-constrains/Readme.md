## Task 6: Resource Constraints and Load Testing

Run a container with specific resource constraints and perform a load test.

1. Create a Dockerfile for a simple Flask web application that performs a CPU-intensive task (e.g., calculating Fibonacci numbers)
2. Build and run the container with CPU and memory constraints
3. Use Apache Benchmark (ab) to perform a load test on the container
4. Monitor the container's resource usage during the load test using `docker stats`
5. Analyze the results

docker build -t flask-fibonacci .
docker run -d --name flask-fibonacci --cpus="1.0" --memory="512m" -p 5000:5000 flask-fibonacci

### ab: The Apache Benchmark tool.

### -n 1000: Specifies the total number of requests to perform for the benchmarking session. In this case, 1000 requests.

### -c 10: Specifies the number of multiple requests to perform at a time (i.e., concurrency level). Here, 10 requests will be sent concurrently.

ab -n 1000 -c 10 http://localhost:5000/

docker stats flask-fibonacci
