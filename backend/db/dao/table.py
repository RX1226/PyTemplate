"""定義 items Table，並提供建表、欄位更新、檢查與刪除功能。"""

from sqlalchemy import Boolean, Column, Float, Integer, MetaData, String, Table, inspect, text

from backend.db.database import engine

metadata = MetaData()

item_table = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("quantity", Integer, nullable=False, server_default=text("0")),
    Column("price", Float, nullable=False, server_default=text("0")),
    Column("is_active", Boolean, nullable=False, server_default=text("1")),
)


def create_table() -> bool:
    already_exists = table_exists()
    item_table.create(bind=engine, checkfirst=True)
    add_missing_columns()
    return not already_exists


def add_missing_columns() -> None:
    columns = {column["name"] for column in inspect(engine).get_columns(item_table.name)}
    definitions = {
        "quantity": "INTEGER NOT NULL DEFAULT 0",
        "price": "FLOAT NOT NULL DEFAULT 0",
        "is_active": "BOOLEAN NOT NULL DEFAULT 1",
    }

    with engine.begin() as connection:
        for name, definition in definitions.items():
            if name not in columns:
                connection.exec_driver_sql(
                    f"ALTER TABLE {item_table.name} ADD COLUMN {name} {definition}"
                )


def table_exists() -> bool:
    return inspect(engine).has_table(item_table.name)


def delete_table() -> bool:
    if not table_exists():
        return False

    item_table.drop(bind=engine)
    return True
