from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.api2 import api2
from backend.api.hello import hello_api

app = FastAPI()
app.include_router(hello_api)
app.include_router(api2)

frontend = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")
