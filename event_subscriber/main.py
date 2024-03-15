import pika


def init_subscriber():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
    return pika.BlockingConnection(parameters)


def on_event(ch, method, properties, body):
    print(f"Received message: {body.decode('utf-8')}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    connection = init_subscriber()
    channel = connection.channel()
    channel.queue_declare(queue='first_queue')

    channel.basic_consume(queue='first_queue', on_message_callback=on_event)

    print('Waiting for messages')
    channel.start_consuming()
