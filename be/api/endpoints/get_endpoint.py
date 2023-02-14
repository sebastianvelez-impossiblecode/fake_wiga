from fastapi import APIRouter

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/alive/")
async def alive():
    """Make request to graphQL api and filter by date and facility."""
    return {"message": "SUCCESS!"}
