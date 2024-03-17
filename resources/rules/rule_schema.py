from pydantic import BaseModel


class Rule(BaseModel):
    id: str
    name: str
    threshold_price: float
    symbol: str
    threshold_exceeded: bool
    is_deleted: bool
    created_at: str


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
