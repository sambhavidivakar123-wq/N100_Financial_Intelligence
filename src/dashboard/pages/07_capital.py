import streamlit as st
import plotly.express as px
import pandas as pd

from src.dashboard.utils.db import load_data


st.title("💰 Capital Allocation Map")


df = load_data()


latest = df.sort_values("year").groupby(
    "ticker"
).tail(1)


def classify(row):

    if row["debt_to_equity"] > 2:
        return "Debt Heavy"

    elif row["free_cash_flow"] > latest["free_cash_flow"].median():
        return "Cash Generator"

    elif row["roe"] > latest["roe"].median():
        return "Quality Compounder"

    elif row["net_profit_margin"] > latest["net_profit_margin"].median():
        return "Profit Leader"

    else:
        return "Stable"


latest["capital_pattern"] = latest.apply(
    classify,
    axis=1
)


fig = px.treemap(
    latest,
    path=[
        "capital_pattern",
        "company_name"
    ],
    values="free_cash_flow",
    title="Capital Allocation Patterns"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader(
    "Companies by Pattern"
)


pattern = st.selectbox(
    "Select Pattern",
    sorted(
        latest["capital_pattern"].unique()
    )
)


st.dataframe(
    latest[
        latest["capital_pattern"] == pattern
    ][
        [
            "company_name",
            "ticker",
            "sector",
            "roe",
            "free_cash_flow"
        ]
    ],
    use_container_width=True
)