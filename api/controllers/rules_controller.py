from resources.rules.rule_service import *
from fastapi import APIRouter, HTTPException, Depends
from db.models.models import get_db
from sqlalchemy.orm import Session
from resources.rules.rule_schema import *
from typing import List
from resources.rules.rule_model import Rule

router = APIRouter()


@router.get("/", response_model=list[RulePydantic])
def get_rules(db: Session = Depends(get_db)):
    try:
        rule_objects = list_rules(db)

        rules = [RulePydantic(id=rule.id, name=rule.name, symbol=rule.symbol, threshold_price=rule.threshold_price,
                      is_deleted=rule.is_deleted, threshold_exceeded=rule.threshold_exceeded,
                      created_at=rule.created_at) for rule in rule_objects]
        return rules

    except Exception as err:
        print("Failed while getting rules")
        print(f"{err}")


@router.post("/", response_model=RulePydantic)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    try:
        new_rule = create_rule_svc(db, rule)
        rule = RulePydantic(id=new_rule.id, name=new_rule.name, symbol=new_rule.symbol, threshold_price=new_rule.threshold_price,
                      is_deleted=new_rule.is_deleted, threshold_exceeded=new_rule.threshold_exceeded,
                      created_at=new_rule.created_at)
        return rule

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.patch("/{rule_id}", response_model=RulePydantic)
def update_rule(rule_id: str, rule: RuleUpdate, db: Session = Depends(get_db)):
    try:
        updated_rule = update_rule_svc(db, rule_id, rule)
        rule = RulePydantic(id=updated_rule.id, name=updated_rule.name, symbol=updated_rule.symbol, threshold_price=updated_rule.threshold_price,
                      is_deleted=updated_rule.is_deleted, threshold_exceeded=updated_rule.threshold_exceeded,
                      created_at=updated_rule.created_at)
        return rule

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