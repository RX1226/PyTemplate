"""提供建立、檢查與刪除 SQLite Database 的 HTTP API。"""

from fastapi import APIRouter

from backend.db.database import (
    DB_PATH,
    create_database,
    database_exists,
    delete_database,
)

router = APIRouter(prefix="/database")


@router.post("")
def create() -> dict[str, str | bool]:
    created = create_database()
    message = "Database created" if created else "Database already exists"
    return {"message": message, "created": created, "path": str(DB_PATH)}


@router.get("")
def status() -> dict[str, str | bool]:
    return {"exists": database_exists(), "path": str(DB_PATH)}


@router.delete("")
def remove() -> dict[str, str | bool]:
    deleted = delete_database()
    message = "Database deleted" if deleted else "Database does not exist"
    return {"message": message, "deleted": deleted}
