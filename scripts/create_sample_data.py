import pandas as pd
import os

# Create data/raw if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

companies = pd.DataFrame({
    "company_id": [1, 2, 3, 4, 5],
    "ticker": ["TCS", "INFY", "RELIANCE", "HDFCBANK", "ITC"],
    "company_name": [
        "Tata Consultancy Services",
        "Infosys",
        "Reliance Industries",
        "HDFC Bank",
        "ITC Limited"
    ],
    "sector": [
        "IT",
        "IT",
        "Energy",
        "Banking",
        "FMCG"
    ]
})

companies.to_excel("data/raw/companies.xlsx", index=False)

print("companies.xlsx created successfully!")