from fastapi import APIRouter

from api.api_v1.endpoints import cycle

api_router = APIRouter()
api_router.include_router(cycle.router, prefix="/cycle", tags=["cycle"])
