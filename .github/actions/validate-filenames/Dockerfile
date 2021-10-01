FROM python:3-slim AS builder
ADD ./src /app
WORKDIR /app

FROM python:3-slim
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["python", "/app/main.py"]