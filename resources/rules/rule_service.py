""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.rules.rule_dal import *


def list_rules(db_session) -> list[Rule]:
    return list_rules_db(db_session)


def create_rule_svc(db_session, rule) -> Rule:
    return create_rule_db(db_session, rule)


def update_rule_svc(db_session, rule_id, rule) -> Rule:
    return update_rule_db(db_session, rule_id, rule)


def delete_rule_svc(db_session, rule_id) -> str:
    return delete_rule_db(db_session, rule_id)
