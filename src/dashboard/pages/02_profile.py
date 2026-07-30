import streamlit as st
import plotly.express as px

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from src.dashboard.utils.db import load_data, get_companies


st.title("🏢 Company Profile")

df = load_data()

companies = get_companies()

company_list = (
    companies["ticker"]
    .sort_values()
    .tolist()
)


ticker = st.selectbox(
    "Search Company / Ticker",
    company_list
)


company_data = df[
    df["ticker"] == ticker
]


if company_data.empty:

    st.error(
        "Ticker not found — please try another"
    )

else:

    latest = company_data.iloc[-1]


    st.subheader(
        latest["company_name"]
    )


    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Sector",
        latest["sector"]
    )

    col2.metric(
        "ROE",
        f"{latest['roe']:.2f}"
    )

    col3.metric(
        "ROCE",
        f"{latest['roce']:.2f}"
    )


    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Net Profit Margin",
        f"{latest['net_profit_margin']:.2f}"
    )

    col5.metric(
        "Debt / Equity",
        f"{latest['debt_to_equity']:.2f}"
    )

    col6.metric(
        "Free Cash Flow",
        f"{latest['free_cash_flow']:.2f}"
    )


    st.subheader(
        "Revenue and Net Profit"
    )


    trend = company_data[
        [
            "year",
            "sales",
            "net_profit"
        ]
    ]


    fig = px.bar(
        trend,
        x="year",
        y=[
            "sales",
            "net_profit"
        ],
        barmode="group",
        title="Financial Performance"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )