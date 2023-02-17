"""API monitor and admin app."""
from datetime import datetime
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every

api = FastAPI(
    title="FAKE WIGA",
    description="API for fake wiga",
)


@api.on_event("startup")
@repeat_every(seconds=10)
def scheduler_test() -> None:
    response = requests.get("http://localhost:8080/weather/alive")


# Cors Settings
origins = [
    "*",
]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .endpoints.weather_data import router as weather
from .endpoints.sensors import router as sensors
from .endpoints.get_endpoint import router as alive

api.include_router(weather)
api.include_router(sensors)
api.include_router(alive)
