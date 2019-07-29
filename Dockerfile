ARG ARCH

FROM ${ARCH}/python:3.7-alpine

ENV VERSION 2.0.0

EXPOSE 8080

RUN mkdir /code

# Python requirements
ADD requirements/* /code/requirements/

RUN apk add --no-cache build-base linux-headers python3-dev && \
    apk add --no-cache postgresql-dev && \
    apk add --no-cache zlib-dev jpeg-dev && \
    python3 -m pip install --no-cache-dir -r /code/requirements/production.txt && \
    apk del build-base linux-headers python3-dev
    
COPY . /code

RUN /code/manage.py collectstatic --noinput

CMD ["/code/docker-entrypoint.sh"]
