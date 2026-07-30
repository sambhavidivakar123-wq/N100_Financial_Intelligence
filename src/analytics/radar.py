from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def normalize(series):
    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series([50] * len(series), index=series.index)

    return ((series - minimum) / (maximum - minimum)) * 100


def generate_radar_charts(df):

    Path("reports/radar_charts").mkdir(
        parents=True,
        exist_ok=True,
    )

    metrics = [
        "roe",
        "roce",
        "net_profit_margin",
        "asset_turnover",
        "free_cash_flow",
        "composite_quality_score",
    ]

    radar_df = df.copy()

    for metric in metrics:
        radar_df[metric] = normalize(radar_df[metric])

    labels = [
        "ROE",
        "ROCE",
        "NPM",
        "Asset Turnover",
        "FCF",
        "Composite",
    ]

    num_vars = len(labels)

    angles = np.linspace(
        0,
        2 * np.pi,
        num_vars,
        endpoint=False,
    ).tolist()

    angles += angles[:1]

    for _, row in radar_df.iterrows():

        values = [row[m] for m in metrics]
        values += values[:1]

        fig, ax = plt.subplots(
            figsize=(6, 6),
            subplot_kw=dict(polar=True),
        )

        ax.plot(angles, values, linewidth=2)
        ax.fill(angles, values, alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)

        ax.set_title(row["company_name"])

        plt.savefig(
            f"reports/radar_charts/{row['ticker']}_radar.png",
            dpi=200,
            bbox_inches="tight",
        )

        plt.close()
        