import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

profit_loss = pd.DataFrame({
    "company_id": [1, 2, 3, 4, 5],
    "year": [2024, 2024, 2024, 2024, 2024],
    "sales": [250000, 180000, 450000, 320000, 90000],
    "operating_profit": [62000, 42000, 98000, 75000, 18000],
    "net_profit": [48000, 33000, 71000, 56000, 14000]
})

profit_loss.to_excel(
    "data/raw/profitandloss.xlsx",
    index=False
)

print("profitandloss.xlsx created successfully!")