""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_dal import *
from sqlalchemy.orm import Session
from fastapi import Depends
from db.models.models import get_db


def list_alerts():
    db_session_generator = get_db()
    try:
        db = next(db_session_generator) 
        return list_alerts_db(db)
    finally:
        next(db_session_generator, None)


def create_alert(alert, db_session):
    return create_alert_db(alert, db_session)
