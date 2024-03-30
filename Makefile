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

consumer-logs:
	docker logs -f consumer_node

worker-logs:
	docker logs -f worker_node

beat-logs:
	docker logs -f beat_node