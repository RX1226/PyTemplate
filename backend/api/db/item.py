"""接收 Item HTTP 請求，並透過 Item DAO 執行資料 CRUD。"""

from fastapi import APIRouter, HTTPException, status

from backend.db.dao import item_dao
from backend.db.models.item import ItemInput

router = APIRouter(prefix="/items")


@router.post("", status_code=status.HTTP_201_CREATED)
def create(data: ItemInput) -> item_dao.ItemData:
    return item_dao.add_item(
        data.name,
        data.quantity,
        data.price,
        data.is_active,
    )


@router.get("")
def read_all() -> list[item_dao.ItemData]:
    return item_dao.get_items()


@router.put("/{item_id}")
def update(item_id: int, data: ItemInput) -> item_dao.ItemData:
    item = item_dao.update_item(
        item_id,
        data.name,
        data.quantity,
        data.price,
        data.is_active,
    )
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}")
def delete(item_id: int) -> dict[str, bool]:
    if not item_dao.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": True}
