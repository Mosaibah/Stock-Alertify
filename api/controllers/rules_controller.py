from resources.alerts.alert_service import list_alerts
from resources.rules.rule_service import *
from fastapi import APIRouter, HTTPException, Depends
from db.models.models import get_db
from sqlalchemy.orm import Session
from resources.rules.rule_schema import *


router = APIRouter()


@router.get("/", response_model=Rule)
def get_rules(db: Session = Depends(get_db)):
    try:
        return list_rules(db)

    except Exception as err:
        print("Failed while getting rules")
        print(f"{err}")


@router.post("/", response_model=Rule)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    try:
        return create_rule_svc(rule, db)

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.patch("/{rule_id}", response_model=Rule)
def update_rule(rule_id: str, rule: RuleUpdate, db: Session = Depends(get_db)):
    try:
        return update_rule_svc(db, rule_id, rule)

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.delete("/{rule_id}")
def delete_rule(rule_id: str, db: Session = Depends(get_db)) -> str:
    try:
        return delete_rule_svc(db, rule_id)

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")