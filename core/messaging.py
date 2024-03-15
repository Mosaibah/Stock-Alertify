from amqpstorm import Connection
from amqpstorm import Message


if __name__ == "__main__":
    with Connection('localhost', 'guest', 'guest') as connection:
        channel = connection.channel()
        channel.queue.declare(queue='first_queue')
        message = Message.create(channel, "هلا والله")
        message.publish('first_queue')
