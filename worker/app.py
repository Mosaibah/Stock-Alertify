# Create a celery app object to start your workers
import logging

from celery import Celery
from resources.market.market_service import get_market_data
from dotenv import load_dotenv
from resources.rules.rule_service import list_rules
from db.models.models import SessionLocal
from sqlalchemy.orm import Session
from resources.rules.rule_model import Rule
from resources.alerts.alert_service import create_alert
from resources.alerts.alert_model import Alert
from core.messaging import send_message

load_dotenv()


def create_celery_app():
    app = Celery(
        'worker',
        broker='amqp://guest:guest@localhost:5672/'
    )
    app.conf.beat_schedule = {
        'every-20-seconds': {
            'task': 'worker.app.process_market_rules_task',
            'schedule': 20
        },
    }
    app.conf.timezone = 'UTC'
    return app


#  Create a celery task that use the market_service.py to fetch the market data
#  use the rules_service.py to get all the users rules
#  Inside the celery publish THRESHOLD_ALERT event if there is a threshold crossover

celery_app = create_celery_app()

# TODO: import it from db
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        print("Failed to connect to database.")
        print(f"{err}")
        raise
    finally:
        db.close()


@celery_app.task
def process_market_rules_task():
    try:
        logging.log(logging.INFO, "processing_market_rules_task started")
        print("processing_market_rules_task started")

        print("get_market_data started")
        market_data = get_market_data()
        print("get_market_data ended")

        db: Session = SessionLocal()

        print("list_rules started")
        rules: list[Rule] = list_rules(db_session=db)
        print("list_rules ended")

        for market in market_data:
            for rule in rules:
                if market.symbol == rule.symbol:
                    if rule.threshold_exceeded:
                        if market.price > rule.threshold_price:
                            msg = f"Publishing THRESHOLD_ALERT for {rule.symbol} and price {market.price}, and threshold {rule.threshold_price}"
                            send_message("morning", msg, alert=Alert(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol))
                    else:
                        if market.price < rule.threshold_price:
                            msg = f"Publishing THRESHOLD_ALERT for {rule.symbol} and price {market.price}, and threshold {rule.threshold_price}"
                            send_message("morning", msg, alert=Alert(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol))


    except Exception as err:
        print(f"Failed to process market rules: {err}")


# process_market_rules_task()