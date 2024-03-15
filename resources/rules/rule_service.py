""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.rules.rule_dal import list_rules_db, create_rule_db, update_rule_db


def list_rules(db_session):
    return list_rules_db(db_session)


def create_rule_svc(db_session, rule):
    return create_rule_db(db_session, rule)


def update_rule_svc(db_session, rule_id, rule):
    return update_rule_db(db_session, rule_id, rule)