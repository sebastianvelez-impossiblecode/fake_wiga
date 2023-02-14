"""API monitor and admin app."""
from fastapi import APIRouter

from ...controllers import weather as weather_controller
from ..api_schemas import WeatherOutSchema, WeatherInSchema

router = APIRouter(prefix="/weather", tags=["weather"])


@router.post("/weather_data/")
async def weather_data(filters: WeatherInSchema):
    """Make request to graphQL api and filter by date and facility."""
    return weather_controller.read_weather_file(filters)
