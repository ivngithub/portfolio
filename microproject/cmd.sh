#!/bin/bash
set -e

if [ "$FLASK_APP" = 'microproject.py' ]; then
  echo "Running Development Server"
  exec flask run  --host=0.0.0.0 --port=5000
else
  echo "Running Production Server"
  exec uwsgi --http 0.0.0.0:5000 --wsgi-file /microproject/microproject.py \
             --callable app --stats 0.0.0.0:9191
fi
