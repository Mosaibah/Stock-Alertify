up:
	./dev_setup/up.sh
down:
	./dev_setup/down.sh
run-api:
	python3 -m venv stock-alertify-env-2 && \
	. stock-alertify-env-2/bin/activate && \
	cp .env.example .env && \
	pip install -r requirements.txt && \
	uvicorn api.main:app --reload

