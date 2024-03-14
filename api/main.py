from fastapi import FastAPI
from api.routes import init_routes
from uvicorn import run

app = init_routes(FastAPI())

if __name__ == "__main__":
    run("api.main:app")
