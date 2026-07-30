import streamlit as st
import plotly.express as px

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_data

st.title("🏠 Nifty 100 Analytics - Home")

df = load_data()

latest_year = df["year"].max()

st.sidebar.header("Year Selection")

year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["year"].unique()),
    index=0
)

year_df = df[df["year"] == year]


# KPI calculations

avg_roe = year_df["roe"].mean()
median_de = year_df["debt_to_equity"].median()
total_companies = year_df["company_id"].nunique()

debt_free = (
    year_df[year_df["debt_to_equity"] == 0]
    ["company_id"]
    .nunique()
)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average ROE",
    f"{avg_roe:.2f}"
)

col2.metric(
    "Median Debt/Equity",
    f"{median_de:.2f}"
)

col3.metric(
    "Total Companies",
    total_companies
)

col4.metric(
    "Debt Free Companies",
    debt_free
)


st.subheader("Sector Breakdown")

sector_count = (
    year_df.groupby("sector")
    ["company_id"]
    .nunique()
    .reset_index()
)


fig = px.pie(
    sector_count,
    names="sector",
    values="company_id",
    title="Companies by Sector"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader("Top Companies by ROE")

top_companies = (
    year_df[
        [
            "company_name",
            "ticker",
            "sector",
            "roe"
        ]
    ]
    .sort_values(
        "roe",
        ascending=False
    )
    .head(5)
)


st.dataframe(
    top_companies,
    use_container_width=True
)