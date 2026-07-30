from pathlib import Path

import pandas as pd

DATA_DIR = Path("data/raw")

companies = pd.read_excel(DATA_DIR / "companies.xlsx")
ratios = pd.read_excel(DATA_DIR / "financial_ratios.xlsx")
pnl = pd.read_excel(DATA_DIR / "profitandloss.xlsx")
balance = pd.read_excel(DATA_DIR / "balancesheet.xlsx")
cashflow = pd.read_excel(DATA_DIR / "cashflow.xlsx")

# Merge yearly datasets
df = ratios.merge(
    pnl,
    on=["company_id", "year"],
    how="left"
)

df = df.merge(
    balance,
    on=["company_id", "year"],
    how="left"
)

df = df.merge(
    cashflow,
    on=["company_id", "year"],
    how="left"
)

df = df.merge(
    companies,
    on="company_id",
    how="left"
)

# ---------- Derived Metrics ----------

df["debt_to_equity"] = (
    df["total_liabilities"] / df["equity"]
)

df["asset_turnover"] = (
    df["sales"] / df["total_assets"]
)

df["net_profit_margin"] = (
    df["net_profit"] / df["sales"] * 100
)

df["free_cash_flow"] = (
    df["operating_cashflow"] +
    df["investing_cashflow"]
)

# Save
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

df.to_excel(
    output_dir / "master_financial_dataset.xlsx",
    index=False,
)

print(df.head())
print("\nSaved to data/processed/master_financial_dataset.xlsx")