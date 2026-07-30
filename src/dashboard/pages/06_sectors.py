import streamlit as st
import plotly.express as px

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_data


st.title("🏭 Sector Analysis")


df = load_data()


sectors = sorted(
    df["sector"]
    .dropna()
    .unique()
)


selected_sector = st.selectbox(
    "Select Sector",
    sectors
)


sector_df = df[
    df["sector"] == selected_sector
]


st.subheader(
    f"{selected_sector} Companies"
)


fig = px.scatter(
    sector_df,
    x="sales",
    y="roe",
    size="total_assets",
    color="company_name",
    hover_name="ticker",
    title="Revenue vs ROE Analysis"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader(
    "Sector Median Metrics"
)


median_df = (
    sector_df[
        [
            "roe",
            "roce",
            "net_profit_margin",
            "debt_to_equity"
        ]
    ]
    .median()
    .reset_index()
)


median_df.columns = [
    "Metric",
    "Median Value"
]


bar = px.bar(
    median_df,
    x="Metric",
    y="Median Value",
    title="Sector Median KPIs"
)


st.plotly_chart(
    bar,
    use_container_width=True
)