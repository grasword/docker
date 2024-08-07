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

## Solution

docker swarm init

docker config create nginx_config_v1 nginx.conf

docker service create --name nginx_service --config source=nginx_config_v1,target=/etc/nginx/nginx.conf -p 80:80 nginx
