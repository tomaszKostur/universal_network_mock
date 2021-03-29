NAME=network_mock_container

docker stop $NAME
docker build --tag=network_mock:dev --file=network_mock_manager.Dockerfile .
docker run --name=$NAME --rm --detach --network=mock_network network_mock:dev
