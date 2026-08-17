from fastapi import APIRouter

router = APIRouter()

@router.get("/peers")
def get_peers():
    return {"message": "Peers endpoint working"}