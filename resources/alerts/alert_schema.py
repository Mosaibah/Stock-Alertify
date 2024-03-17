""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from pydantic import BaseModel


class Alert(BaseModel):
    id: str
    name: str
    threshold_price: float
    symbol: str
    is_deleted: bool
    created_at: str


class AlertCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
