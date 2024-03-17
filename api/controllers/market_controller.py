import requests
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from resources.market.market_service import get_market_data
from resources.market.market_schema import Market


load_dotenv()

router = APIRouter()


@router.get("/", response_model=Market)
async def get_market_price():
    try:
        market_data = get_market_data()
        return market_data

    except HTTPException as err:
        raise err
