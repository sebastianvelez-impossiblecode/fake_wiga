from fastapi import APIRouter
from ..api_schemas import SensorsOutSchema

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/sensors/")
async def sensors() -> list[SensorsOutSchema]:
    """Make request."""
    sensor_ids = [
        {"id": 330, "Nombre": "Humedad Relativa EST Caribe - Antioquia %", "otra_vaina": 42},
        {
            "id": 331,
            "Nombre": "Radiación Par EST Caribe - Antioquia µmol m-2 s-1",
            "otra_vaina": 42,
        },
        {"id": 332, "Nombre": "Temperatura EST Caribe - Antioquia °C", "otra_vaina": 42},
    ]

    return sensor_ids
