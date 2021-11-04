FROM python:latest

RUN apt update
RUN apt install -y git

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /app/entrypoint.sh
COPY process-input.py /app/process-input.py
WORKDIR /app

# Executes `entrypoint.sh` when the Docker container starts up 
CMD ["/app/entrypoint.sh"]