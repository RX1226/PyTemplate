"""提供建立、檢查與刪除 items Table 的 HTTP API。"""

from fastapi import APIRouter

from backend.db.dao.table import create_table, delete_table, item_table, table_exists

router = APIRouter(prefix="/table")


@router.post("")
def create() -> dict[str, str | bool]:
    created = create_table()
    message = "Table created" if created else "Table already exists"
    return {"message": message, "created": created, "table": item_table.name}


@router.get("")
def status() -> dict[str, str | bool]:
    return {"exists": table_exists(), "table": item_table.name}


@router.delete("")
def remove() -> dict[str, str | bool]:
    deleted = delete_table()
    message = "Table deleted" if deleted else "Table does not exist"
    return {"message": message, "deleted": deleted, "table": item_table.name}
