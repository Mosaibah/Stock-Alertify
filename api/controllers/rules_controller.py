import logging

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
        logging.log(logging.INFO, "List_rules started")
        rules_data = list_rules(db)
        logging.log(logging.INFO, "List_rules started")
        return rules_data

    except Exception as err:
        print("Failed while getting rules")
        print(f"{err}")


@router.post("/", response_model=RulePydantic)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    try:
        logging.log(logging.INFO, "Create_rule started")
        rule_data = create_rule_svc(db, rule)
        logging.log(logging.INFO, "Create_rule ended")
        return rule_data

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.patch("/{rule_id}", response_model=RulePydantic)
def update_rule(rule_id: str, rule: RuleUpdate, db: Session = Depends(get_db)):
    try:
        logging.log(logging.INFO, "Update_rule started")
        rule_data = update_rule_svc(db, rule_id, rule)
        logging.log(logging.INFO, "Update_rule ended")
        return rule_data

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")


@router.delete("/{rule_id}")
def delete_rule(rule_id: str, db: Session = Depends(get_db)) -> str:
    try:
        logging.log(logging.INFO, "Delete_rule started")
        id_deleted = delete_rule_svc(db, rule_id)
        logging.log(logging.INFO, "Delete_rule ended")
        return id_deleted

    except Exception as err:
        print("Failed while creating rule")
        print(f"{err}")
        raise HTTPException(status_code=400, detail=f"Failed while creating rule: {err}")