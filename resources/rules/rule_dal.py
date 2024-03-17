""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.rules.rule_model import Rule
from resources.rules.rule_schema import RuleUpdate
from fastapi import HTTPException


def list_rules_db(db_session) -> list[Rule]:
    # TODO: implement pagination

    rules = db_session.query(Rule).filter(Rule.is_deleted.is_(None)).all()
    return rules


def create_rule_db(rule, db_session) -> Rule:
    try:
        rule_object = Rule(name=rule.name, threshold_price=rule.threshold_price,
                           symbol=rule.symbol, threshold_exceeded=rule.threshold_exceeded)
        db_session.add(rule_object)
        db_session.commit()
        db_session.refresh(rule_object)
        return rule_object

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


def update_rule_db(db_session, rule_id: str, rule: RuleUpdate) -> Rule:
    try:
        rule_object = db_session.query(Rule).filter(Rule.id == rule_id).first()
        if rule_object is None:
            raise HTTPException(status_code=401, detail="Rule not found")

        if rule.name is not None:
            rule_object.name = rule.name
        if rule.threshold_price is not None:
            rule_object.threshold_price = rule.threshold_price
        if rule.symbol is not None:
            rule_object.symbol = rule.symbol
        if rule.threshold_price is not None:
            rule_object.threshold_price = rule.threshold_price

        db_session.commit()
        db_session.refresh(rule_object)
        return rule_object

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


def delete_rule_db(db_session, rule_id: str) -> str:
    try:
        rule_object = db_session.query(Rule).filter(Rule.id == rule_id).first()
        if rule_object is None:
            raise HTTPException(status_code=401, detail="Rule not found")

        rule_object.is_deleted = True
        db_session.commit()
        db_session.refresh(rule_object)
        return "Rule deleted successfully"

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

