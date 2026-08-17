from fastapi import APIRouter
import sqlite3
import time

router = APIRouter()

START_TIME = time.time()


@router.get("/health")
def health():
    conn = sqlite3.connect("database/nifty100.db")
    cur = conn.cursor()

    tables = [
        "companies",
        "profitandloss",
        "balancesheet",
        "cashflow",
        "financial_ratios",
        "stock_prices",
        "sectors",
        "analysis",
    ]

    counts = {}

    for table in tables:
        counts[table] = cur.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]

    conn.close()

    return {
        "status": "ok",
        "db_row_counts": counts,
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "version": "1.0.0",
    }