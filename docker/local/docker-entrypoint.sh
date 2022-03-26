#!/bin/sh
set -e
. /venv/bin/activate

[ ! -f "/store/docker/local/vars.env" ] \
&& echo 'Unable to find docker/local/vars.env' \
&& exit 1

while read -r line; do
    echo $line | grep . | grep -v '^#' && export $line
done < /store/docker/local/vars.env

# /wait && gunicorn --reload store.wsgi --workers 1 --bind 0.0.0.0:8000 --timeout 360 --log-level debug --preload
export FLASK_ENV=development
export FLASK_APP='api/app.py'
/wait && flask run --host=0.0.0.0 --port=8000