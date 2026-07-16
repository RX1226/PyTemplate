"""集中註冊純 API 與會存取資料庫的 API router。"""

from fastapi import APIRouter

from backend.api.db.database import router as database_router
from backend.api.db.item import router as item_router
from backend.api.db.table import router as table_router
from backend.api.http.api2 import router as api2_router
from backend.api.http.hello import router as hello_router

api_router = APIRouter(prefix="/api")
api_router.include_router(hello_router)
api_router.include_router(api2_router)
api_router.include_router(database_router)
api_router.include_router(table_router)
api_router.include_router(item_router)
