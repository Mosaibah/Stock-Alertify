""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.rules.rule_model import Rule


def list_rules_db(db_session):
    # TODO: implement pagination

    rules = db_session.query(Rule).all()
    return rules


def create_rules_db(rule, db_session):
    rule_object = Rule(name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol)
    db_session.add(rule_object)
    db_session.commit()
    db_session.refresh(rule_object)
    return rule_object
