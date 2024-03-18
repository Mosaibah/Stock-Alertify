SHELL := /bin/bash
VENV := stock-alertify-env-2
VENV_BIN := $(VENV)/bin
PYTHON := $(VENV_BIN)/python
PIP := $(VENV_BIN)/pip

export PYTHONPATH := $(shell pwd)

.PHONY: up down run-api start-consumer publish-event run-worker run-beat setup-env install-deps

up:
	./dev_setup/up.sh

down:
	./dev_setup/down.sh

setup-env:
	python3 -m venv $(VENV)

install-deps: setup-env
	$(VENV)/bin/pip install -r requirements.txt

run-api: install-deps
	$(VENV)/bin/uvicorn api.main:app --reload

start-consumer: set-env
	$(VENV)/bin/python event_subscriber/main.py

publish-event: set-env
	$(VENV)/bin/python core/messaging.py

start-worker: set-env
	$(VENV)/bin/celery -A worker.app.celery_app worker --loglevel=info

start-beat: set-env
	$(VENV)/bin/celery -A worker.app.celery_app beat --loglevel=info

set-env:
	@if [ -d "$(VENV)" ]; then \
		 . $(VENV)/bin/activate; \
	else \
		echo "Virtual environment not found. Run 'make setup-env' first."; \
	fi
