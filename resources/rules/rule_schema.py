from pydantic import BaseModel
from typing import Optional


class RuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str


class RuleUpdate(BaseModel):
    name: str | None = None
    threshold_price: float | None = None
    symbol: str | None = None
