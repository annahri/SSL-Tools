#!/bin/sh

cd src && gunicorn --bind 127.0.0.1:8000 ssl-tools.wsgi &

exec "$@"
