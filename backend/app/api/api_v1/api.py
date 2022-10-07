from fastapi import APIRouter

from app.api.api_v1.endpoints import health, item

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(item.router, prefix="/items", tags=["items"])