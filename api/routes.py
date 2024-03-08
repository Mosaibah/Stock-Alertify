from fastapi import APIRouter
from controllers.market_controller import get_market_price

router = APIRouter()

router.get("/market-price", response_model=dict)(get_market_price)
