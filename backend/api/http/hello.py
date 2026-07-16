"""提供最簡單、不存取資料庫的 Hello API 範例。"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}
