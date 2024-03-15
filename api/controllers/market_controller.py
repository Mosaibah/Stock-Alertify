import requests
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from resources.market.market_service import get_market_data


load_dotenv()

router = APIRouter()


@router.get("/")
async def get_market_price():
    try:
        market_data = get_market_data()
        return market_data

    except HTTPException as err:
        raise err
