#!/bin/sh

set -e

if [ "$SQL_ENGINE" = "django.db.backends.postgresql" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

uv run python manage.py migrate --noinput
uv run python manage.py collectstatic --no-input --clear

exec "$@"
