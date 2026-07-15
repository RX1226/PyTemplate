from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.routes import api_router

app = FastAPI()
app.include_router(api_router)

frontend = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")
