import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

# -----------------------------
# Balance Sheet
# -----------------------------
balancesheet = pd.DataFrame({
    "company_id": [1, 2, 3, 4, 5],
    "year": [2024]*5,
    "total_assets": [500000, 420000, 900000, 700000, 200000],
    "total_liabilities": [180000, 150000, 420000, 310000, 80000],
    "equity": [320000, 270000, 480000, 390000, 120000]
})

balancesheet.to_excel(
    "data/raw/balancesheet.xlsx",
    index=False
)

# -----------------------------
# Cash Flow
# -----------------------------
cashflow = pd.DataFrame({
    "company_id": [1, 2, 3, 4, 5],
    "year": [2024]*5,
    "operating_cashflow": [70000, 51000, 120000, 93000, 25000],
    "investing_cashflow": [-25000, -18000, -60000, -35000, -9000],
    "financing_cashflow": [-12000, -10000, -20000, -15000, -5000]
})

cashflow.to_excel(
    "data/raw/cashflow.xlsx",
    index=False
)

print("balancesheet.xlsx created")
print("cashflow.xlsx created")