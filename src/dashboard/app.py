import streamlit as st

st.set_page_config(
    page_title="Nifty 100 Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 Nifty 100 Analytics Platform")

st.sidebar.title("Navigation")

st.sidebar.info(
    """
    Welcome to N100 Financial Intelligence.

    Dashboard modules:
    - Home
    - Company Profile
    - Screener
    - Peer Comparison
    - Trends
    - Sector Analysis
    - Capital Allocation
    - Reports
    """
)

st.subheader("Dashboard Status")

st.success("Streamlit dashboard scaffold is running successfully!")

st.write(
    """
    Sprint 4 Dashboard Foundation

    The following modules will be added:
    - Company analytics
    - Screener
    - Peer comparison
    - Valuation analysis
    """
)