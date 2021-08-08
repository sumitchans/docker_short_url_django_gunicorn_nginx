#!/bin/bash

cd urlshortener_service

python manage.py makemigrations --no-input
python manage.py migrate --no-input

gunicorn url_shortener_service.wsgi:application \
  --name ubuntu \
  --workers 5 \
  --bind 0.0.0.0:8000 \
  -k sync\
  --log-level=debug \
  --max-requests 50\
  --max-requests-jitter 10\
  --graceful-timeout 60\
  --log-file "/opt/urlshortener_service/logs/gunicorn.error" \
  --timeout 60 \
  --threads 5
