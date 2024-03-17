""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AlertPydantic(BaseModel):
    id: UUID
    name: str
    threshold_price: float
    symbol: str
    created_at: datetime


class AlertCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
