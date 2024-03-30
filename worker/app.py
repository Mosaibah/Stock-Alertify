# Create a celery app object to start your workers
import logging
from celery.schedules import crontab
from celery import Celery
from resources.market.market_service import get_market_data
from dotenv import load_dotenv
from resources.rules.rule_service import list_rules
from db.models.models import SessionLocal
from resources.rules.rule_model import Rule
from resources.alerts.alert_model import Alert
from core.messaging import send_message
import os

load_dotenv()

user = os.getenv('RABBITMQ_USER')
password = os.getenv('RABBITMQ_PASSWORD')
host = os.getenv('RABBITMQ_HOST')


def create_celery_app():
    app = Celery(
        'worker',
        broker='amqp://'+user+':'+password+'@'+host+':5672/'
    )
    app.conf.beat_schedule = {
        'every-30-minutes': {
            'task': 'worker.app.process_market_rules_task',
            'schedule': crontab(minute='*/30'),
        },
    }
    app.conf.timezone = 'UTC'
    return app


#  Create a celery task that use the market_service.py to fetch the market data
#  use the rules_service.py to get all the users rules
#  Inside the celery publish THRESHOLD_ALERT event if there is a threshold crossover

celery_app = create_celery_app()


@celery_app.task
def process_market_rules_task():
    try:
        logging.log(logging.INFO, "processing_market_rules_task started")

        logging.log(logging.INFO, "get_market_data started")
        market_data = get_market_data()
        logging.log(logging.INFO, "get_market_data ended")

        logging.log(logging.INFO, "list_rules started")
        rules: list[Rule] = list_rules(db_session=SessionLocal())
        logging.log(logging.INFO, "list_rules ended")

        # index rules
        rules_by_symbol = {}
        for rule in rules:
            if rule.symbol not in rules_by_symbol:
                rules_by_symbol[rule.symbol] = []
            rules_by_symbol[rule.symbol].append(rule)

        for market in market_data:
            if market.symbol in rules_by_symbol:
                for rule in rules_by_symbol[market.symbol]:
                    should_publish_alert = False
                    if rule.threshold_exceeded:
                        if market.price > rule.threshold_price:
                            should_publish_alert = True
                    else:
                        if market.price < rule.threshold_price:
                            should_publish_alert = True

                    if should_publish_alert:
                        msg = f"Publishing THRESHOLD_ALERT for {rule.symbol} and price {market.price}, and threshold {rule.threshold_price}"
                        logging.log(logging.INFO, msg)
                        send_message("alert_queue", msg, alert=Alert(name=rule.name, threshold_price=rule.threshold_price,
                                                                 symbol=rule.symbol))
    except Exception as err:
        print(f"Failed to process market rules: {err}")
