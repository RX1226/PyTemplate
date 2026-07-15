from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api import api2, hello_api

app = FastAPI()
app.include_router(hello_api)
app.include_router(api2)

frontend = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")
