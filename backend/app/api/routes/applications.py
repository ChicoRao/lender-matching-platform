from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_applications() -> str:
    return "Got applications"