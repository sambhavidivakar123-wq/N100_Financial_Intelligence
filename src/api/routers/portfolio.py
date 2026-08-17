from fastapi import APIRouter

router = APIRouter()

@router.get("/portfolio/stats")
def get_portfolio_stats():
    return {"message": "Portfolio endpoint working"}