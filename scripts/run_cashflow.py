from pathlib import Path

import pandas as pd

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
    capital_allocation_pattern,
)

INPUT_FILE = Path("data/processed/master_financial_dataset.xlsx")
OUTPUT_FILE = Path("output/cashflow_intelligence.xlsx")
DISTRESS_FILE = Path("output/distress_alerts.csv")


def main():
    df = pd.read_excel(INPUT_FILE)

    records = []

    for _, row in df.iterrows():

        fcf = free_cash_flow(
            row["operating_cashflow"],
            row["investing_cashflow"],
        )

        cfo_score, cfo_label = cfo_quality_score(
            row["operating_cashflow"],
            row["net_profit"],
        )

        capex_pct, capex_label = capex_intensity(
            row["investing_cashflow"],
            row["sales"],
        )

        fcf_conversion = fcf_conversion_rate(
            fcf,
            row["operating_profit"],
        )

        allocation = capital_allocation_pattern(
            row["operating_cashflow"],
            row["investing_cashflow"],
            row["financing_cashflow"],
            cfo_score,
        )

        distress = (
            row["operating_cashflow"] < 0
            and row["financing_cashflow"] > 0
        )

        records.append({
            "company_id": row["company_id"],
            "company_name": row["company_name"],
            "sector": row["sector"],
            "free_cash_flow": fcf,
            "cfo_quality_score": cfo_score,
            "cfo_quality_label": cfo_label,
            "capex_intensity_pct": capex_pct,
            "capex_label": capex_label,
            "fcf_conversion_pct": fcf_conversion,
            "capital_allocation": allocation,
            "distress_flag": distress,
        })

    output = pd.DataFrame(records)

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    output.to_excel(OUTPUT_FILE, index=False)

    output[output["distress_flag"]].to_csv(
        DISTRESS_FILE,
        index=False,
    )

    print(f"Saved: {OUTPUT_FILE}")
    print(f"Saved: {DISTRESS_FILE}")


if __name__ == "__main__":
    main()