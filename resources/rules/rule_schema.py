from pydantic import BaseModel


class RuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
