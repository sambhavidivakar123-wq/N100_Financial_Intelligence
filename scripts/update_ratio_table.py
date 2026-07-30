import sqlite3

conn = sqlite3.connect("database/nifty100.db")
cursor = conn.cursor()

columns = [
    ("net_profit_margin_pct", "REAL"),
    ("operating_profit_margin_pct", "REAL"),
    ("return_on_assets_pct", "REAL"),
    ("free_cash_flow", "REAL"),
]

for column_name, column_type in columns:
    try:
        cursor.execute(
            f"ALTER TABLE financial_ratios ADD COLUMN {column_name} {column_type}"
        )
        print(f"Added {column_name}")
    except sqlite3.OperationalError:
        print(f"{column_name} already exists")

conn.commit()
conn.close()

print("Table updated successfully!")