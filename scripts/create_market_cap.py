import pandas as pd
from pathlib import Path


input_file = "data/processed/master_financial_dataset.xlsx"
output_file = "data/processed/market_cap.xlsx"


df = pd.read_excel(input_file)


latest = (
    df.sort_values("year")
    .groupby("ticker")
    .tail(1)
)


# Derived market cap proxy
# (used because actual market cap data is not available)

latest["market_cap"] = (
    latest["equity"].abs() * 20
)


market_cap_df = latest[
    [
        "company_id",
        "company_name",
        "ticker",
        "sector",
        "market_cap"
    ]
]


Path("data/processed").mkdir(
    exist_ok=True
)


market_cap_df.to_excel(
    output_file,
    index=False
)


print(
    f"Saved: {output_file}"
)