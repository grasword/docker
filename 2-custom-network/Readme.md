## Task 2: Custom Bridge Network and Container Communication

Create two containers that can communicate over a custom bridge network.

1. Create a custom bridge network
2. Run an Alpine container with a custom name on this network
3. Run another Alpine container on the same network
4. Demonstrate communication between the containers using `ping`

docker network create -d bridge custom_network
docker run -d --name alpine1 --network custom_network alpine sleep 1000
docker run -d --name alpine2 --network custom_network alpine sleep 1000
docker exec alpine1 ping -c 10 alpine2

bridge - creates private lan
host - uses host network
