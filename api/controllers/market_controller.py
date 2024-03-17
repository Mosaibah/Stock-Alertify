import logging

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from resources.market.market_service import get_market_data
from resources.market.market_schema import Market


load_dotenv()

router = APIRouter()


@router.get("/", response_model=list[Market])
async def get_market_price():
    try:
        logging.log(logging.INFO, "get_market_data started")
        market_data = get_market_data()
        logging.log(logging.INFO, "get_market_data ended")

        return market_data

    except Exception as err:
        print("Failed while getting alerts")
        print(f"{err}")
