from resources.alerts.alert_service import list_alerts
from resources.rules.rule_service import *
from fastapi import APIRouter, HTTPException, Depends
from db.models.models import SessionLocal
from sqlalchemy.orm import Session
from resources.rules.rule_schema import RuleCreate, RuleUpdate


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
def get_rules(db: Session = Depends(get_db)):
    try:
        return list_rules(db)

    except Exception as err:
        print("Failed while getting rules")
        print(f"{err}")


@router.post("/")
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    try:
        return create_rule_svc(rule, db)

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.patch("/{rule_id}")
def update_rule(rule_id: str, rule: RuleUpdate, db: Session = Depends(get_db)):
    try:
        return update_rule_svc(db, rule_id, rule)

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.delete("/{rule_id}")
def delete_rule(rule_id: str, db: Session = Depends(get_db)):
    try:
        return delete_rule_svc(db, rule_id)

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")