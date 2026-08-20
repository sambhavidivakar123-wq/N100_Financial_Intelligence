from fastapi import APIRouter
import pandas as pd

router = APIRouter()

PORTFOLIO_FILE = "output/portfolio_stats.csv"


@router.get("/portfolio/stats")
def get_portfolio_stats():
    return {"message": "Portfolio endpoint working"}


@router.get("/portfolio")
def get_portfolio():
    try:
        df = pd.read_csv(PORTFOLIO_FILE)

        return {
            "count": len(df),
            "portfolio": df.fillna("").to_dict(orient="records"),
        }

    except FileNotFoundError:
        return {
            "count": 0,
            "portfolio": [],
            "message": "Portfolio statistics file not found",
        }
