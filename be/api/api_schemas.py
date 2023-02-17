"""Schemas for by_date_and_facility endpoint in Kronos api."""
from pydantic import BaseModel
from typing import Optional


class WeatherInSchema(BaseModel):
    """GET(/orders/) Payload Model."""

    ids_sensores: list[int]
    fecha_inicio: str
    fecha_fin: str

    class Config:
        """Example default schema."""

        schema_extra = {
            "example": {
                "ids_sensores": [330, 331, 332],
                "fecha_inicio": "2020-01-26 00:00:01",
                "fecha_fin": "2020-01-26 10:00:01",
            }
        }


class WeatherOutSchema(BaseModel):
    """GET(/orders/) Response Model."""

    sensors: list[dict]


class SensorsOutSchema(BaseModel):
    """GET(/sensors/) Response Model."""

    id: int
    Nombre: str
    otra_vaina: int
