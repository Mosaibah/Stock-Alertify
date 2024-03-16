""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from resources.alerts.alert_model import Alert
from resources.alerts.alert_schema import AlertCreate


def list_alerts_db(db_session):
    # TODO: implement pagination
    
    alerts = db_session.query(Alert).all()
    return alerts


def create_alert_db(alert: AlertCreate, db_session):
    alert_object = Alert(name=alert.name, threshold_price=alert.threshold_price, symbol=alert.symbol)
    db_session.add(alert_object)
    db_session.commit()
    db_session.refresh(alert_object)
    return alert_object
