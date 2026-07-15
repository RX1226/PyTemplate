from fastapi import APIRouter

api2 = APIRouter(prefix="/api")


@api2.get("/api2")
def get_api2() -> dict[str, str]:
    return {"message": "Hello from API 2!"}
