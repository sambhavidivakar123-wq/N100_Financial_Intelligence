import sqlite3
import pandas as pd

conn = sqlite3.connect("database/nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow"
]

for table in tables:
    print(f"\n===== {table.upper()} =====")
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    print(df)

conn.close()