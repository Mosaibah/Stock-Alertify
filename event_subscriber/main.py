import json

import pika
from resources.alerts.alert_service import create_alert
from resources.alerts.alert_model import Alert
from db.models.models import SessionLocal


def init_subscriber():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    return pika.BlockingConnection(parameters)


def on_event(ch, method, properties, body):
    print(f"Received message: {body.decode('utf-8')}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

    alert_json = json.loads(body)['alert']

    try:
        create_alert(alert=Alert(name=alert_json['name'], threshold_price=alert_json['threshold_price'],
                                 symbol=alert_json['symbol']), db_session=SessionLocal())
    except Exception as err:
        print(f"Failed to create alert: {err}")


if __name__ == "__main__":
    connection = init_subscriber()
    channel = connection.channel()
    channel.queue_declare(queue='alert_queue')

    channel.basic_consume(queue='alert_queue', on_message_callback=on_event)

    print('Waiting for messages')
    channel.start_consuming()
