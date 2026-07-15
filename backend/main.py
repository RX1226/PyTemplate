from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api import hello_api

app = FastAPI()
app.include_router(hello_api)

frontend = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")
