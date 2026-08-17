from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


INPUT_FILE = "data/processed/master_financial_dataset.xlsx"

FEATURES = [
    "roe",
    "debt_to_equity",
    "asset_turnover",
    "net_profit_margin",
    "free_cash_flow",
]


def main():
    df = pd.read_excel(INPUT_FILE)

    Path("reports").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)

    # Correlation matrix
    corr = df[FEATURES].corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(corr)
    plt.colorbar()
    plt.xticks(range(len(FEATURES)), FEATURES, rotation=45)
    plt.yticks(range(len(FEATURES)), FEATURES)
    plt.tight_layout()
    plt.savefig("reports/correlation_heatmap.png")
    plt.close()

    # Portfolio statistics
    stats = pd.DataFrame({
        "P10": df[FEATURES].quantile(0.10),
        "P25": df[FEATURES].quantile(0.25),
        "P50": df[FEATURES].quantile(0.50),
        "P75": df[FEATURES].quantile(0.75),
        "P90": df[FEATURES].quantile(0.90),
        "Mean": df[FEATURES].mean(),
        "Std": df[FEATURES].std(),
    })

    stats.to_csv("output/portfolio_stats.csv")

    # Outlier detection
    outliers = []

    for feature in FEATURES:
        mean = df[feature].mean()
        std = df[feature].std()

        if std == 0:
            continue

        z = (df[feature] - mean) / std

        flagged = df.loc[
            abs(z) > 2,
            ["company_id", "company_name"]
        ].copy()

        flagged["metric"] = feature
        flagged["z_score"] = z[abs(z) > 2].values

        outliers.append(flagged)

    if outliers:
        pd.concat(outliers).to_csv(
            "output/outlier_report.csv",
            index=False,
        )
    else:
        pd.DataFrame(
            columns=[
                "company_id",
                "company_name",
                "metric",
                "z_score",
            ]
        ).to_csv(
            "output/outlier_report.csv",
            index=False,
        )

    print("Saved: reports/correlation_heatmap.png")
    print("Saved: output/portfolio_stats.csv")
    print("Saved: output/outlier_report.csv")


if __name__ == "__main__":
    main()