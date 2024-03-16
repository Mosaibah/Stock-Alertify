# Create a celery app object to start your workers
from celery import Celery
from resources.market.market_service import get_market_data
from dotenv import load_dotenv
from resources.rules.rule_service import list_rules
from db.models.models import SessionLocal
from sqlalchemy.orm import Session
from resources.rules.rule_model import Rule
from resources.alerts.alert_service import create_alert
from resources.alerts.alert_model import Alert


load_dotenv()


def create_celery_app():
    app = Celery(
        'worker',
        broker='amqp://guest:guest@rabbitmq-node:5672/'
    )
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
                            print(f"Publishing THRESHOLD_ALERT for {rule.symbol} and price {market.price}, and threshold {rule.threshold_price}")
                            new = create_alert(Alert(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol), db_session=db)
                    else:
                        if market.price < rule.threshold_price:
                            print(f"Publishing THRESHOLD_ALERT for {rule.symbol} and price {market.price} and threshold {rule.threshold_price}")
                            new = create_alert(Alert(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol), db_session=db)






    except Exception as err:
        print(f"Failed to process market rules: {err}")


process_market_rules_task()