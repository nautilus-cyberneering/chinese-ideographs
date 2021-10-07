FROM python:3.9

RUN pip install dvc

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Executes `entrypoint.sh` when the Docker container starts up 
ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]