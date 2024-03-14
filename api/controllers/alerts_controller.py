from resources.alerts.alert_service import list_alerts
from resources.rules.rule_service import list_rules, create_rule_svc
from fastapi import APIRouter, HTTPException, Depends
from db.models.models import SessionLocal
from sqlalchemy.orm import Session


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


@router.get("/")
def alerts(db: Session = Depends(get_db)):
    try:
        return list_alerts(db)

    except Exception as err:
        print("Failed while getting alerts")
        print(f"{err}")
