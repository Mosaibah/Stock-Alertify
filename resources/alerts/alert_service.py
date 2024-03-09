""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_dal import create_alert

def create_new_alert( rule: AlertCreate, session ):
    return create_alert( rule=rule, session=session)
