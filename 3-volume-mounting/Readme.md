## Task 3: Volume Mounting and Data Persistence

Use volume mounting to persist data between container runs.

1. Create a Docker volume
2. Run a container that mounts this volume and writes data to it
3. Stop and remove the container
4. Run a new container that mounts the same volume
5. Verify that the data persists

docker volume create sw_reference
docker run -d --name sw_container -v sw_reference:/data busybox sh -c "echo 'General Kenobi!' > /data/helloThere.txt"

docker stop sw_container
docker rm sw_container

docker run --rm -v sw_reference:/data busybox cat /data/helloThere.txt
