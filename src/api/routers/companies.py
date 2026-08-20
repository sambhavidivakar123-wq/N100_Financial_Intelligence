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

@router.get("/companies/{ticker}/pl")
def get_profit_and_loss(ticker: str):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT p.*
    FROM profitandloss p
    JOIN companies c
        ON p.company_id = c.company_id
    WHERE UPPER(c.ticker) = UPPER(?)
    ORDER BY p.year
    """

    df = pd.read_sql(query, conn, params=[ticker])
    conn.close()

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker}' not found"
        )

    return df.to_dict(orient="records")

@router.get("/companies/{ticker}/bs")
def get_balance_sheet(ticker: str):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT b.*
    FROM balancesheet b
    JOIN companies c
        ON b.company_id = c.company_id
    WHERE UPPER(c.ticker) = UPPER(?)
    ORDER BY b.year
    """

    df = pd.read_sql(query, conn, params=[ticker])
    conn.close()

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker}' not found"
        )

    return df.to_dict(orient="records")

@router.get("/companies/{ticker}/cashflow")
def get_cashflow(ticker: str):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT cf.*
    FROM cashflow cf
    JOIN companies c
        ON cf.company_id = c.company_id
    WHERE UPPER(c.ticker) = UPPER(?)
    ORDER BY cf.year
    """

    df = pd.read_sql(query, conn, params=[ticker])
    conn.close()

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker}' not found"
        )

    return df.to_dict(orient="records")

@router.get("/companies/{ticker}/ratios")
def get_ratios(ticker: str):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT fr.*
    FROM financial_ratios fr
    JOIN companies c
        ON fr.company_id = c.company_id
    WHERE UPPER(c.ticker) = UPPER(?)
    ORDER BY fr.year
    """

    df = pd.read_sql(query, conn, params=[ticker])
    conn.close()

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Ticker '{ticker}' not found"
        )

    return df.to_dict(orient="records")