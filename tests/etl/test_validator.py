import sqlite3
import pandas as pd


def test_companies_table_exists():
    conn = sqlite3.connect("database/nifty100.db")

    tables = pd.read_sql(
        "SELECT name FROM sqlite_master WHERE type='table';",
        conn
    )

    conn.close()

    assert "companies" in tables["name"].values


def test_profitandloss_table_exists():
    conn = sqlite3.connect("database/nifty100.db")

    tables = pd.read_sql(
        "SELECT name FROM sqlite_master WHERE type='table';",
        conn
    )

    conn.close()

    assert "profitandloss" in tables["name"].values


def test_company_records_exist():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    assert len(df) > 0


def test_profitandloss_records_exist():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT * FROM profitandloss",
        conn
    )

    conn.close()

    assert len(df) > 0

def test_no_missing_company_names():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT company_name FROM companies",
        conn
    )

    conn.close()

    assert df["company_name"].isnull().sum() == 0


def test_positive_sales():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT sales FROM profitandloss",
        conn
    )

    conn.close()

    assert (df["sales"] > 0).all()


def test_positive_stock_prices():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT close_price FROM stock_prices",
        conn
    )

    conn.close()

    assert (df["close_price"] > 0).all()


def test_unique_company_ids():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT company_id FROM companies",
        conn
    )

    conn.close()

    assert df["company_id"].is_unique

def test_no_duplicate_tickers():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT ticker FROM companies",
        conn
    )

    conn.close()

    assert df["ticker"].is_unique


def test_company_count():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    assert len(df) == 5


def test_profit_loss_has_year():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT year FROM profitandloss",
        conn
    )

    conn.close()

    assert df["year"].notnull().all()


def test_balance_sheet_has_assets():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT total_assets FROM balancesheet",
        conn
    )

    conn.close()

    assert (df["total_assets"] > 0).all()


def test_cashflow_not_empty():
    conn = sqlite3.connect("database/nifty100.db")

    df = pd.read_sql(
        "SELECT * FROM cashflow",
        conn
    )

    conn.close()

    assert len(df) > 0
def test_balance_sheet_has_liabilities():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT total_liabilities FROM balancesheet", conn)
    conn.close()
    assert (df["total_liabilities"] >= 0).all()


def test_balance_sheet_has_equity():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT equity FROM balancesheet", conn)
    conn.close()
    assert (df["equity"] >= 0).all()


def test_stock_price_dates_exist():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT date FROM stock_prices", conn)
    conn.close()
    assert df["date"].notnull().all()


def test_sectors_not_empty():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT * FROM sectors", conn)
    conn.close()
    assert len(df) > 0


def test_analysis_not_empty():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT * FROM analysis", conn)
    conn.close()
    assert len(df) > 0


def test_financial_ratios_not_empty():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT * FROM financial_ratios", conn)
    conn.close()
    assert len(df) > 0


def test_ticker_values_not_blank():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT ticker FROM companies", conn)
    conn.close()
    assert (df["ticker"].str.strip() != "").all()


def test_sector_values_not_blank():
    conn = sqlite3.connect("database/nifty100.db")
    df = pd.read_sql("SELECT sector FROM companies", conn)
    conn.close()
    assert (df["sector"].str.strip() != "").all()
