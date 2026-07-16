"""封裝 items Table 的新增、查詢、修改與刪除操作。"""

from sqlalchemy import delete, insert, select, update

from backend.db.database import engine
from backend.db.dao.table import item_table


ItemData = dict[str, int | float | str | bool]


def add_item(
    name: str,
    quantity: int = 0,
    price: float = 0,
    is_active: bool = True,
) -> ItemData:
    with engine.begin() as connection:
        result = connection.execute(
            insert(item_table).values(
                name=name,
                quantity=quantity,
                price=price,
                is_active=is_active,
            )
        )
        item_id = result.inserted_primary_key[0]
    return {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "is_active": is_active,
    }


def get_items() -> list[ItemData]:
    with engine.connect() as connection:
        rows = connection.execute(
            select(item_table).order_by(item_table.c.id)
        ).mappings()
        return [dict(row) for row in rows]


def update_item(
    item_id: int,
    name: str,
    quantity: int,
    price: float,
    is_active: bool,
) -> ItemData | None:
    with engine.begin() as connection:
        result = connection.execute(
            update(item_table)
            .where(item_table.c.id == item_id)
            .values(
                name=name,
                quantity=quantity,
                price=price,
                is_active=is_active,
            )
        )
        if result.rowcount == 0:
            return None
    return {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "is_active": is_active,
    }


def delete_item(item_id: int) -> bool:
    with engine.begin() as connection:
        result = connection.execute(
            delete(item_table).where(item_table.c.id == item_id)
        )
        return result.rowcount > 0
