""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""

from pydantic import BaseModel, Field
import uuid

class AlertCreate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str 
    threshold_price: float
    symbol: str