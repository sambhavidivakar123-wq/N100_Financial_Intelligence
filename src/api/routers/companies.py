from fastapi import APIRouter, HTTPException
import sqlite3
import pandas as pd

router = APIRouter()

DB_PATH = "database/nifty100.db"


@router.get("/companies")
def get_companies():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT c.company_id,
           c.ticker,
           c.company_name,
           c.sector,
           fr.roe,
           fr.roce
    FROM companies c
    LEFT JOIN financial_ratios fr
    ON c.company_id = fr.company_id
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_dict(orient="records")


@router.get("/companies/{ticker}")
def get_company(ticker: str):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT c.company_id,
           c.ticker,
           c.company_name,
           c.sector,
           fr.*
    FROM companies c
    LEFT JOIN financial_ratios fr
    ON c.company_id = fr.company_id
    WHERE UPPER(c.ticker) = UPPER(?)
    """

    df = pd.read_sql(query, conn, params=[ticker])

    conn.close()

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker}' not found"
        )

    return df.iloc[0].to_dict()