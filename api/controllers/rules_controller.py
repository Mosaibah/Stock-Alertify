from resources.alerts.alert_service import list_alerts
from resources.rules.rule_service import list_rules
from fastapi import APIRouter, HTTPException, Depends
from db.models.models import SessionLocal
from sqlalchemy.orm import Session

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
        return list_alerts(db)

    except Exception as err:
        print("Failed to connect to database.")
        print(f"{err}")


def get_rules(db: Session = Depends(get_db)):
    try:
        return list_rules(db)

    except Exception as err:
        print("Failed to connect to database.")
        print(f"{err}")

