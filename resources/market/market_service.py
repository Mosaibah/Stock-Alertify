""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
import os
import requests
from resources.market.market_schema import Market
from fastapi import HTTPException


def get_market_data() -> list[Market]:
    url = "https://twelve-data1.p.rapidapi.com/price"

    # TODO: make it dynamic
    querystring = {"symbol": "AAPL, MSFT, GOOG, AMZN, META", "format": "json", "outputsize": "30"}
    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        prices = []  # type: list[Market]

        for symbol, info in data.items():
            price_value = float(info['price'])
            prices.append(Market(symbol=symbol, price=price_value))
        return prices

    except requests.RequestException as err:
        raise HTTPException(status_code=400, detail=f"Error fetching market data: {err}")
