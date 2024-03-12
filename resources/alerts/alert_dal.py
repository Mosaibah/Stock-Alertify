""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from resources.alerts.alert_model import Alert


def list_alerts_db(db_session):
    ## TODO: implement pagination
    
    alerts = db_session.query(Alert).all()
    return alerts
