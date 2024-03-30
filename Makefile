.PHONY: up down consumer-logs worker-logs beat-logs publish-event

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

publish-event:
	docker exec -it fastapi_app_node /bin/bash -c "python3 core/messaging.py"