import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

async def get_market_price():
    url = "https://twelve-data1.p.rapidapi.com/price"
    querystring = {"symbol":"AAPL, MSFT, GOOG, AMZN, META","format":"json","outputsize":"30"}
    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }
        
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status() 
        return response.json()
    
    except requests.RequestException as err:
        raise HTTPException(status_code=400, detail=f"Error fetching market data: {err}")
