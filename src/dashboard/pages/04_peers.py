import streamlit as st
import plotly.graph_objects as go

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_data


st.title("🤝 Peer Comparison")


df = load_data()


# Peer group selection

sectors = (
    df["sector"]
    .dropna()
    .unique()
    .tolist()
)


sector = st.selectbox(
    "Select Peer Group",
    sorted(sectors)
)


peer_df = df[
    df["sector"] == sector
]


ticker = st.selectbox(
    "Select Company",
    peer_df["ticker"].unique()
)


company = peer_df[
    peer_df["ticker"] == ticker
].iloc[-1]


metrics = [
    "roe",
    "roce",
    "net_profit_margin",
    "debt_to_equity",
    "asset_turnover",
    "free_cash_flow"
]


company_values = [
    company[m]
    for m in metrics
]


average_values = [
    peer_df[m].mean()
    for m in metrics
]


fig = go.Figure()


fig.add_trace(
    go.Scatterpolar(
        r=company_values,
        theta=metrics,
        fill="toself",
        name=ticker
    )
)


fig.add_trace(
    go.Scatterpolar(
        r=average_values,
        theta=metrics,
        fill="toself",
        name="Peer Average"
    )
)


fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader(
    "Peer Group Comparison"
)


table = peer_df[
    [
        "company_name",
        "ticker",
        "roe",
        "roce",
        "net_profit_margin",
        "debt_to_equity"
    ]
]


st.dataframe(
    table,
    use_container_width=True
)