"""提供第二支不存取資料庫的 API 範例。"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/api2")
def get_api2() -> dict[str, str]:
    return {"message": "Hello from API 2!"}
