from pathlib import Path

import pandas as pd
import streamlit as st


DATA_FILE = Path(
    "data/processed/master_financial_dataset.xlsx"
)


@st.cache_data(ttl=600)
def load_data():
    return pd.read_excel(DATA_FILE)


@st.cache_data(ttl=600)
def get_companies():
    df = load_data()

    return (
        df[
            [
                "company_id",
                "company_name",
                "ticker",
                "sector",
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )


@st.cache_data(ttl=600)
def get_ratios(ticker, year=None):
    df = load_data()

    result = df[df["ticker"] == ticker]

    if year:
        result = result[result["year"] == year]

    return result


@st.cache_data(ttl=600)
def get_pl(ticker):
    df = load_data()

    return df[df["ticker"] == ticker][
        [
            "year",
            "sales",
            "operating_profit",
            "net_profit",
        ]
    ]


@st.cache_data(ttl=600)
def get_cf(ticker):
    df = load_data()

    return df[df["ticker"] == ticker][
        [
            "year",
            "operating_cashflow",
            "investing_cashflow",
            "financing_cashflow",
            "free_cash_flow",
        ]
    ]


@st.cache_data(ttl=600)
def get_sectors():
    df = load_data()

    return (
        df["sector"]
        .drop_duplicates()
        .sort_values()
        .tolist()
    )


@st.cache_data(ttl=600)
def get_peers(group_name):
    df = load_data()

    return df[df["sector"] == group_name]


@st.cache_data(ttl=600)
def get_valuation(ticker):
    df = load_data()

    return df[df["ticker"] == ticker]