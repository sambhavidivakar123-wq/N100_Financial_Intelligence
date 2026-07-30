import streamlit as st
import pandas as pd

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_data


st.title("🔍 Company Screener")


df = load_data()


st.sidebar.header("Filters")


roe_min = st.sidebar.slider(
    "Minimum ROE",
    float(df["roe"].min()),
    float(df["roe"].max()),
    float(df["roe"].min())
)


de_max = st.sidebar.slider(
    "Maximum Debt/Equity",
    float(df["debt_to_equity"].min()),
    float(df["debt_to_equity"].max()),
    float(df["debt_to_equity"].max())
)


fcf_min = st.sidebar.slider(
    "Minimum Free Cash Flow",
    float(df["free_cash_flow"].min()),
    float(df["free_cash_flow"].max()),
    float(df["free_cash_flow"].min())
)


filtered = df[
    (df["roe"] >= roe_min)
    &
    (df["debt_to_equity"] <= de_max)
    &
    (df["free_cash_flow"] >= fcf_min)
]


st.subheader(
    f"{len(filtered)} companies match your filters"
)


display = filtered[
    [
        "company_id",
        "company_name",
        "ticker",
        "sector",
        "roe",
        "debt_to_equity",
        "free_cash_flow"
    ]
]


st.dataframe(
    display,
    use_container_width=True
)


csv = display.to_csv(
    index=False
)


st.download_button(
    "Download CSV",
    csv,
    "screener_results.csv",
    "text/csv"
)