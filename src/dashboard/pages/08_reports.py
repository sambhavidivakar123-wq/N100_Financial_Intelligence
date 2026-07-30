import streamlit as st

from src.dashboard.utils.db import load_data


st.title("📄 Annual Reports")


df = load_data()


companies = sorted(
    df["ticker"].unique()
)


ticker = st.selectbox(
    "Search Company",
    companies
)


company = df[
    df["ticker"] == ticker
].iloc[-1]


st.subheader(
    company["company_name"]
)


st.write(
    f"Sector: {company['sector']}"
)


st.subheader(
    "Available Annual Reports"
)


available_years = sorted(
    df[
        df["ticker"] == ticker
    ]["year"]
    .unique(),
    reverse=True
)


for year in available_years:

    st.write(
        f"📘 Annual Report {year}"
    )

    st.warning(
        "Report unavailable - PDF link not available"
    )