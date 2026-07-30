import streamlit as st
import plotly.express as px

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_data


st.title("📈 Trend Analysis")


df = load_data()


ticker = st.selectbox(
    "Select Company",
    sorted(df["ticker"].unique())
)


company_df = df[
    df["ticker"] == ticker
]


metrics = st.multiselect(
    "Select Metrics",
    [
        "sales",
        "net_profit",
        "roe",
        "roce",
        "free_cash_flow"
    ],
    default=[
        "sales",
        "net_profit"
    ]
)


if metrics:

    chart_df = company_df[
        ["year"] + metrics
    ]

    fig = px.line(
        chart_df,
        x="year",
        y=metrics,
        markers=True,
        title=f"{ticker} Trend Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "Select at least one metric"
    )


st.subheader("Available Data")

st.write(
    f"Available years: {sorted(company_df['year'].unique())}"
)