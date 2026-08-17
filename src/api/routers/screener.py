from fastapi import APIRouter

router = APIRouter()

@router.get("/screener")
def get_screener():
    return {
        "message": "Screener endpoint working"
    }