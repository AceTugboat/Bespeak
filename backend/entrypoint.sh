#!/bin/sh

USER_ID=${UID:-1001}
GROUP_ID=${GID:-1001}

echo "Starting with UID: $USER_ID, GID: $GROUP_ID"

# Fix permissions
chown -R "$USER_ID":"$GROUP_ID" /config

# Run the command as the specified user
gosu "$USER_ID":"$GROUP_ID" "$@"

# Start the backend
until cd /app/backend
do
    echo "Waiting for backend volume..."
    sleep 1
done

until python manage.py migrate --noinput
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput

uvicorn bespeak.asgi:application --host 0.0.0.0 --port 8000 --reload
