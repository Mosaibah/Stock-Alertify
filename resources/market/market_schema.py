""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""
from pydantic import BaseModel


class Market(BaseModel):
    symbol: str
    price: float
