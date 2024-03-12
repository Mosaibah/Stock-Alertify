from fastapi import FastAPI
from api.routes import router as market_router

app = FastAPI()

app.include_router(market_router)
