from fastapi import FastAPI
import requests
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/market-price")
async def getMarketPrice():
    url = "https://twelve-data1.p.rapidapi.com/price"

    querystring = {"symbol":"AAPL, MSFT, GOOG, AMZN, META","format":"json","outputsize":"30"}

    headers = {
        "X-RapidAPI-Key": os.environ['RAPID-API-KEY'],
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()
    
