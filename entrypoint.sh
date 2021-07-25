#!/bin/bash

while ! </dev/tcp/$POSTGRES_HOST/$POSTGRES_PORT; do
  sleep 3
done
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
