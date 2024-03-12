""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_dal import list_alerts_db


def list_alerts(db_session):
    return list_alerts_db(db_session)
