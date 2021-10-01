FROM python:3-slim AS builder
ADD ./src /app
WORKDIR /app

FROM python:3-slim AS linting
RUN pip install --upgrade autopep8
ADD ./src /app
# Fail when autopep8 finds errors:
# https://es.stackoverflow.com/questions/487904/make-autopep8-fail-in-a-docker-build
RUN autopep8 -rd /app && if [ ! -z "$(autopep8 -rd /app)" ]; then exit 1; fi

FROM python:3-slim
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["python", "/app/main.py"]