#!/bin/bash

# Start the FastAPI app with Uvicorn in the background
uvicorn api.main:app --host 0.0.0.0 --port 8000 &

# Start the consumer script in the foreground (to keep the container running)
python3 event_subscriber/main.py
