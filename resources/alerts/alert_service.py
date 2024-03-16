""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_dal import *


def list_alerts(db_session):
    return list_alerts_db(db_session)


def create_alert(alert, db_session):
    return create_alert_db(alert, db_session)
