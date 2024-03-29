#!/bin/bash

uvicorn api.main:app --host 0.0.0.0 --port 8000 &

python3 event_subscriber/main.py &

celery -A worker.app.celery_app worker --loglevel=info --detach &

celery -A worker.app.celery_app beat --loglevel=info --detach
