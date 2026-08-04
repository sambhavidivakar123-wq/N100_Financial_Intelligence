from pathlib import Path

import pandas as pd

INPUT_FILE = Path("data/processed/master_financial_dataset.xlsx")
OUTPUT_FILE = Path("output/pros_cons_summary.xlsx")


def generate_pros_cons(row):
    pros = []
    cons = []

    # ROE
    if row["roe"] >= 20:
        pros.append("High ROE indicates efficient use of shareholder capital.")
    elif row["roe"] < 15:
        cons.append("ROE is relatively low.")

    # ROCE
    if row["roce"] >= 20:
        pros.append("Strong ROCE reflects efficient capital allocation.")
    elif row["roce"] < 15:
        cons.append("ROCE is below the preferred level.")

    # Debt to Equity
    if row["debt_to_equity"] <= 0.5:
        pros.append("Low debt-to-equity ratio indicates a healthy balance sheet.")
    elif row["debt_to_equity"] > 1:
        cons.append("High debt-to-equity ratio increases financial risk.")

    # Net Profit Margin
    if row["net_profit_margin"] >= 15:
        pros.append("Healthy profit margins indicate good profitability.")
    else:
        cons.append("Profit margins could be improved.")

    # Free Cash Flow
    if row["free_cash_flow"] > 0:
        pros.append("Positive free cash flow supports future growth.")
    else:
        cons.append("Negative free cash flow is a concern.")

    score = len(pros) - len(cons)

    if score >= 4:
        recommendation = "Strong Buy"
    elif score >= 2:
        recommendation = "Buy"
    elif score >= 0:
        recommendation = "Hold"
    else:
        recommendation = "Avoid"

    return pd.Series({
        "Pros": "; ".join(pros) if pros else "-",
        "Cons": "; ".join(cons) if cons else "-",
        "Recommendation": recommendation
    })


def main():
    df = pd.read_excel(INPUT_FILE)

    df[["Pros", "Cons", "Recommendation"]] = df.apply(
    generate_pros_cons,
    axis=1
)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(OUTPUT_FILE, index=False)

    print(f"Pros & Cons summary exported to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()