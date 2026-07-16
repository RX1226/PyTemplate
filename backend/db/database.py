"""設定 SQLite 路徑與 SQLAlchemy Engine，並管理 DB 檔案。"""

from pathlib import Path

from sqlalchemy import create_engine

DB_DIR = Path(__file__).parent / "data"
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "app.db"
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

def create_database() -> bool:
    already_exists = DB_PATH.exists()
    with engine.connect() as connection:
        connection.exec_driver_sql("SELECT 1")
    return not already_exists


def database_exists() -> bool:
    return DB_PATH.exists()


def delete_database() -> bool:
    engine.dispose()
    if not DB_PATH.exists():
        return False

    DB_PATH.unlink()
    return True
