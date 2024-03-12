""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.rules.rule_model import Rule


def list_rules_db(db_session):
    ## TODO: implement pagination

    rules = db_session.query(Rule).all()
    return rules
