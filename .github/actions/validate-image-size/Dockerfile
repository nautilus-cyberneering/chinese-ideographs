FROM python:3.9 AS builder
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y libvips-dev 

RUN pip install pyvips
ADD ./src /app
WORKDIR /app

FROM builder AS linting
RUN pip install --upgrade autopep8
# Fail when autopep8 finds errors:
# https://es.stackoverflow.com/questions/487904/make-autopep8-fail-in-a-docker-build
RUN autopep8 -rd /app && if [ ! -z "$(autopep8 -rd /app)" ]; then exit 1; fi

FROM builder
COPY --from=builder /app /app
RUN rm -rf /app/test
ENV PYTHONPATH /app
CMD ["python", "/app/main.py"]
