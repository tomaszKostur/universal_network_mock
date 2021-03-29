FROM python:3
WORKDIR /network_mock_manager
COPY universal_mock.py .
ENTRYPOINT [ "python", "universal_mock.py" ]