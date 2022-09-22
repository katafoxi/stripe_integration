#!/bin/sh

python manage.py migrate
if [ "$DJANGO_SUPERUSER_USERNAME" ];
then
  python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
fi
exec "$@"
