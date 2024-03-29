FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

RUN chmod +x ./dev_setup/start.sh

CMD ["./dev_setup/start.sh"]
