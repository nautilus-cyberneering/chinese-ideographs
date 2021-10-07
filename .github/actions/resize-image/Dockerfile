FROM python:3-slim AS builder
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y libvips-dev 

RUN pip install pyvips
ADD ./src /app
WORKDIR /app


FROM builder
COPY --from=builder /app /app
RUN rm -rf /app/test
ENV PYTHONPATH /app
CMD ["python", "/app/main.py"]
