from fastapi import APIRouter

hello_api = APIRouter(prefix="/api")


@hello_api.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}
