from pathlib import Path

import pandas as pd

INPUT_FILE = Path("data/raw/analysis.xlsx")
OUTPUT_DIR = Path("output")
PARSED_FILE = OUTPUT_DIR / "analysis_parsed.csv"
FAILURE_FILE = OUTPUT_DIR / "parse_failures.csv"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"{INPUT_FILE} not found.")

    OUTPUT_DIR.mkdir(exist_ok=True)

    df = pd.read_excel(INPUT_FILE)

    expected_columns = [
        "compounded_sales_growth",
        "compounded_profit_growth",
        "stock_price_cagr",
        "roe",
    ]

    available = [c for c in expected_columns if c in df.columns]
    missing = [c for c in expected_columns if c not in df.columns]

    if available:
        parsed = df[["company_id"] + available]
        parsed.to_csv(PARSED_FILE, index=False)
    else:
        pd.DataFrame(columns=["company_id", "metric_type", "period_years", "value_pct"]).to_csv(
            PARSED_FILE,
            index=False,
        )

    pd.DataFrame(
        {
            "missing_expected_columns": missing
        }
    ).to_csv(FAILURE_FILE, index=False)

    print("Analysis parser completed.")
    print(f"Parsed output : {PARSED_FILE}")
    print(f"Failure log   : {FAILURE_FILE}")


if __name__ == "__main__":
    main()