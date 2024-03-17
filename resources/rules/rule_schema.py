from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class RulePydantic(BaseModel):
    id: UUID
    name: str
    threshold_price: float
    symbol: str
    threshold_exceeded: bool
    is_deleted: bool | None
    created_at: datetime


class RuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
    threshold_exceeded: bool


class RuleUpdate(BaseModel):
    name: str | None = None
    threshold_price: float | None = None
    symbol: str | None = None
    threshold_exceeded: bool | None = None
