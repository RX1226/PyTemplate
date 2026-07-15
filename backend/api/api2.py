from fastapi import APIRouter

router = APIRouter()


@router.get("/api2")
def get_api2() -> dict[str, str]:
    return {"message": "Hello from API 2!"}
