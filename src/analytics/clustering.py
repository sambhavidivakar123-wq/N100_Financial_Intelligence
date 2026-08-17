from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


FEATURES = [
    "roe",
    "debt_to_equity",
    "net_profit_margin",
    "asset_turnover",
    "free_cash_flow",
]


def run_clustering():
    df = pd.read_excel("data/processed/master_financial_dataset.xlsx")

    cluster_df = df[
        ["company_id", "company_name", "sector"] + FEATURES
    ].copy()

    cluster_df[FEATURES] = cluster_df[FEATURES].fillna(
        cluster_df[FEATURES].median()
    )

    scaler = StandardScaler()
    X = scaler.fit_transform(cluster_df[FEATURES])

    inertias = []

    for k in range(2, 6):
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10,
        )
        model.fit(X)
        inertias.append(model.inertia_)

    Path("reports").mkdir(exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.plot(range(2, 6), inertias, marker="o")
    plt.title("Elbow Plot")
    plt.xlabel("Clusters")
    plt.ylabel("Inertia")
    plt.tight_layout()
    plt.savefig("reports/elbow_plot.png")
    plt.close()

    model = KMeans(
        n_clusters=min(5, len(cluster_df)),
        random_state=42,
        n_init=10,
    )

    labels = model.fit_predict(X)

    distances = model.transform(X).min(axis=1)

    cluster_df["cluster_id"] = labels
    cluster_df["distance_from_centroid"] = distances

    cluster_names = {
        0: "High Quality",
        1: "Growth Leaders",
        2: "Value Picks",
        3: "Cash Generators",
        4: "Emerging Players",
    }

    cluster_df["cluster_name"] = (
        cluster_df["cluster_id"].map(cluster_names)
    )

    Path("output").mkdir(exist_ok=True)

    cluster_df[
        [
            "company_id",
            "company_name",
            "cluster_id",
            "cluster_name",
            "distance_from_centroid",
        ]
    ].to_csv(
        "output/cluster_labels.csv",
        index=False,
    )

    print("Saved: reports/elbow_plot.png")
    print("Saved: output/cluster_labels.csv")