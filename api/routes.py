from fastapi import APIRouter
from api.controllers.market_controller import get_market_price
from api.controllers.rules_controller import alerts

router = APIRouter()

router.get("/market-price", response_model=dict)(get_market_price)
router.get("/alerts")(alerts)
