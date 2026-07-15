from fastapi import APIRouter

from backend.api.api2 import router as api2_router
from backend.api.hello import router as hello_router

api_router = APIRouter(prefix="/api")
api_router.include_router(hello_router)
api_router.include_router(api2_router)
