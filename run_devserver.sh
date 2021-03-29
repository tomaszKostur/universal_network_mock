docker run --rm -it --entrypoint bash -v $(pwd):/opt/shared_sources --network mock_network --name devserver python:3
