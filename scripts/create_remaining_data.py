import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

# -----------------------------
# Financial Ratios
# -----------------------------
financial_ratios = pd.DataFrame({
    "company_id": [1,2,3,4,5],
    "year": [2024]*5,
    "roe": [18.5,21.2,16.8,17.9,19.3],
    "roce": [24.2,26.4,22.1,23.0,25.5],
    "eps": [135.4,72.6,118.3,91.2,16.8]
})

financial_ratios.to_excel(
    "data/raw/financial_ratios.xlsx",
    index=False
)

# -----------------------------
# Stock Prices
# -----------------------------
stock_prices = pd.DataFrame({
    "company_id":[1,2,3,4,5],
    "date":[
        "2024-12-31",
        "2024-12-31",
        "2024-12-31",
        "2024-12-31",
        "2024-12-31"
    ],
    "close_price":[4250,1765,2890,1685,475]
})

stock_prices.to_excel(
    "data/raw/stock_prices.xlsx",
    index=False
)

# -----------------------------
# Sectors
# -----------------------------
sectors = pd.DataFrame({
    "sector_id":[1,2,3,4],
    "sector_name":[
        "IT",
        "Banking",
        "Energy",
        "FMCG"
    ]
})

sectors.to_excel(
    "data/raw/sectors.xlsx",
    index=False
)

# -----------------------------
# Analysis
# -----------------------------
analysis = pd.DataFrame({
    "company_id":[1,2,3,4,5],
    "rating":[5,4,5,4,4],
    "recommendation":[
        "Buy",
        "Buy",
        "Strong Buy",
        "Hold",
        "Buy"
    ]
})

analysis.to_excel(
    "data/raw/analysis.xlsx",
    index=False
)

print("Remaining sample datasets created successfully!")