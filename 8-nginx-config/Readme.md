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

# Step 1: Create an initial Nginx configuration file

echo "server {
listen 80;
server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
    }

}" > default.conf

# Step 2: Create a Docker config from this file

docker config create nginx_config_v1 default.conf

# Step 3: Run an Nginx container using this config

docker service create --name nginx_service --config source=nginx_config_v1,target=/etc/nginx/conf.d/default.conf -p 8080:80 nginx

# Step 4: Test the server

curl http://localhost:8080

# Step 5: Create an updated Nginx configuration file

echo "server {
listen 80;
server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
        try_files \$uri \$uri/ =404;
    }

    location /hello {
        return 200 'Hello, World!';
        add_header Content-Type text/plain;
    }

}" > updated.conf

# Step 6: Create a new Docker config

docker config create nginx_config_v2 updated.conf

# Step 7: Update the running container to use the new config

docker service update --config-rm nginx_config_v1 --config-add source=nginx_config_v2,target=/etc/nginx/conf.d/default.conf nginx_service

# Step 8: Test the server again to see the updated response

curl http://localhost:8080/hello
