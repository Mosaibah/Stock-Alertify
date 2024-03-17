import json

from amqpstorm import Connection
from amqpstorm import Message
from resources.alerts.alert_model import Alert


def send_message(queue, message, alert: Alert = None):
    with Connection('localhost', 'guest', 'guest') as connection:
        channel = connection.channel()
        channel.queue.declare(queue=queue)
        message_content = {
                           "event": "THRESHOLD_ALERT",
                           "message": message,
                           "alert": {
                               "name": alert.name,
                               "threshold_price": alert.threshold_price,
                               "symbol": alert.symbol}
                           }
        message = Message.create(channel, json.dumps(message_content))
        message.publish(queue)


if __name__ == "__main__":
    send_message('alert_queue', 'Hala Hala Wallah !', alert=Alert(name="test", threshold_price=100, symbol="BTC"))

