from resources.alerts.alert_service import list_alerts
from fastapi import APIRouter, HTTPException, Depends
from db.models.models import SessionLocal
from sqlalchemy.orm import Session
from resources.alerts.alert_model import Alert
from typing import List


router = APIRouter()


# Dependency
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


def alerts(db: Session = Depends(get_db)):
    try:
        all_rules = list_alerts(db)
        return all_rules

    except Exception as err:
        print("Failed to connect to database.")
        print(f"{err}")
