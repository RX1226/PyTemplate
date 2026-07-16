"""建立 FastAPI 應用程式，掛載所有 API 與前端靜態頁面。"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.routes import api_router

app = FastAPI()
app.include_router(api_router)

frontend = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")
