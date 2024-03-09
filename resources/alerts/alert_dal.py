""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""

from sqlalchemy.orm import Session
from db.models.models import Alert
from resources.alert.alert_schema import AlertCreate

def create_alert(alert_data: AlertCreate, db_session: Session) -> Alert:
    new_alert = Alert(
        name=alert_data.name,
        threshold_price=alert_data.threshold_price,
        symbol=alert_data.symbol
    )
    db_session.add(new_alert)
    db_session.commit()
    db_session.refresh(new_alert)
    return new_alert
