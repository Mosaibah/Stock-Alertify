""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.rules.rule_model import Rule
from resources.rules.rule_schema import RuleUpdate


def list_rules_db(db_session):
    # TODO: implement pagination

    rules = db_session.query(Rule).all()
    return rules


def create_rule_db(rule, db_session):
    try:
        rule_object = Rule(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol)
        db_session.add(rule_object)
        db_session.commit()
        db_session.refresh(rule_object)
        return rule_object

    except Exception as err:
        return None, str(err)


def update_rule_db(db_session, rule_id: str, rule: RuleUpdate):
    try:
        rule_object = db_session.query(Rule).filter(Rule.id == rule_id).first()
        if rule_object is None:
            return None, "Rule not found"

        if rule.name is not None:
            rule_object.name = rule.name
        if rule.threshold_price is not None:
            rule_object.threshold_price = rule.threshold_price
        if rule.symbol is not None:
            rule_object.symbol = rule.symbol

        db_session.commit()
        db_session.refresh(rule_object)
        return rule_object

    except Exception as err:
        return None, str(err)
