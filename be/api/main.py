"""API monitor and admin app."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(
    title="FAKE WIGA",
    description="API for fake wiga",
)

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
from .endpoints.get_endpoint import router as alive

api.include_router(weather)
api.include_router(alive)
