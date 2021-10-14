FROM python:3.9 AS builder
COPY ./src /app
WORKDIR /app

FROM python:3.9 AS linting
RUN pip install --no-cache-dir --upgrade autopep8==1.5
COPY ./src /app
WORKDIR /app
# Fail when autopep8 finds errors:
# https://es.stackoverflow.com/questions/487904/make-autopep8-fail-in-a-docker-build
RUN autopep8 -rd . && if [ -n "$(autopep8 -rd /app)" ]; then exit 1; fi

FROM python:3.9 AS testing
RUN pip install --no-cache-dir pytest==6.2
COPY ./src /app
WORKDIR /app
RUN pytest

FROM python:3.9
COPY --from=builder /app /app
RUN rm -rf /app/test
ENV PYTHONPATH /app
CMD ["python", "/app/main.py"]