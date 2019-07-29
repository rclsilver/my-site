#!/bin/sh

/code/manage.py migrate

gunicorn \
    --chdir /code \
    -w 5 \
    --bind=0.0.0.0:8080 \
    --access-logfile=- \
    --timeout=30 \
    my_site.wsgi:application
