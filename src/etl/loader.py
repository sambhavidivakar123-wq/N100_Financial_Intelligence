import sqlite3
import pandas as pd

from datetime import datetime
import os

from src.etl.normaliser import normalize_ticker, normalize_text, normalize_year

conn = sqlite3.connect("database/nifty100.db")

os.makedirs("output", exist_ok=True)

load_audit = []


def load_table(excel_file, table_name, preprocess=None):
    """
    Generic function to load an Excel file into a SQLite table.
    """

    df = pd.read_excel(excel_file)

    if preprocess:
        df = preprocess(df)

    # Clear existing data
    conn.execute(f"DELETE FROM {table_name}")

    # Load data
    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )
    load_audit.append({
    "table_name": table_name,
    "rows_loaded": len(df),
    "status": "SUCCESS",
    "load_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})

    print(f"Loaded {len(df)} rows into {table_name}")


# -----------------------------
# Companies
# -----------------------------
def preprocess_companies(df):
    df["ticker"] = df["ticker"].apply(normalize_ticker)
    df["company_name"] = df["company_name"].apply(normalize_text)
    df["sector"] = df["sector"].apply(normalize_text)
    return df


# -----------------------------
# Profit & Loss
# -----------------------------
def preprocess_profit(df):
    df["year"] = df["year"].apply(normalize_year)
    return df


# -----------------------------
# Balance Sheet
# -----------------------------
def preprocess_balance(df):
    df["year"] = df["year"].apply(normalize_year)
    return df


# -----------------------------
# Cash Flow
# -----------------------------
def preprocess_cash(df):
    df["year"] = df["year"].apply(normalize_year)
    return df


# Load all tables
load_table(
    "data/raw/companies.xlsx",
    "companies",
    preprocess_companies
)

load_table(
    "data/raw/profitandloss.xlsx",
    "profitandloss",
    preprocess_profit
)

load_table(
    "data/raw/balancesheet.xlsx",
    "balancesheet",
    preprocess_balance
)

load_table(
    "data/raw/cashflow.xlsx",
    "cashflow",
    preprocess_cash
)

print("\nETL completed successfully!")

datasets = [
    {
        "file": "data/raw/companies.xlsx",
        "table": "companies",
        "preprocess": preprocess_companies
    },
    {
        "file": "data/raw/profitandloss.xlsx",
        "table": "profitandloss",
        "preprocess": preprocess_profit
    },
    {
        "file": "data/raw/balancesheet.xlsx",
        "table": "balancesheet",
        "preprocess": preprocess_balance
    },
    {
        "file": "data/raw/cashflow.xlsx",
        "table": "cashflow",
        "preprocess": preprocess_cash
    },
    {
        "file": "data/raw/financial_ratios.xlsx",
        "table": "financial_ratios",
        "preprocess": preprocess_profit
    },
    {
        "file": "data/raw/stock_prices.xlsx",
        "table": "stock_prices",
        "preprocess": None
    },
    {
        "file": "data/raw/sectors.xlsx",
        "table": "sectors",
        "preprocess": None
    },
    {
        "file": "data/raw/analysis.xlsx",
        "table": "analysis",
        "preprocess": None
    }
]

for dataset in datasets:
    load_table(
        dataset["file"],
        dataset["table"],
        dataset["preprocess"]
    )

conn.commit()

audit_df = pd.DataFrame(load_audit)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print("\nload_audit.csv generated successfully.")

conn.close()

print("\nETL completed successfully!")