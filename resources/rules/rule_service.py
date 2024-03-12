""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.rules.rule_dal import list_rules_db


def list_rules(db_session):
    return list_rules_db(db_session)
