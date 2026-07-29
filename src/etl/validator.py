import sqlite3
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

conn = sqlite3.connect("database/nifty100.db")

validation_results = []


def add_result(rule, severity, table_name, status, message):
    validation_results.append({
        "Rule": rule,
        "Severity": severity,
        "Table": table_name,
        "Status": status,
        "Message": message
    })


# -------------------------
# DQ-01 : Primary Key Check
# -------------------------

companies = pd.read_sql("SELECT * FROM companies", conn)

if companies["company_id"].duplicated().any():
    add_result(
        "DQ-01",
        "CRITICAL",
        "companies",
        "FAIL",
        "Duplicate company_id found."
    )
else:
    add_result(
        "DQ-01",
        "CRITICAL",
        "companies",
        "PASS",
        "Primary Key is unique."
    )


# -------------------------
# DQ-02 : Duplicate Ticker
# -------------------------

if companies["ticker"].duplicated().any():
    add_result(
        "DQ-02",
        "WARNING",
        "companies",
        "FAIL",
        "Duplicate ticker found."
    )
else:
    add_result(
        "DQ-02",
        "WARNING",
        "companies",
        "PASS",
        "Ticker values are unique."
    )


# -------------------------
# DQ-03 : Missing Values Check
# -------------------------

missing = companies.isnull().sum()

if missing.sum() > 0:
    add_result(
        "DQ-03",
        "CRITICAL",
        "companies",
        "FAIL",
        f"Missing values found: {missing.to_dict()}"
    )
else:
    add_result(
        "DQ-03",
        "CRITICAL",
        "companies",
        "PASS",
        "No missing values."
    )
# -------------------------
# DQ-04 : Foreign Key Check
# -------------------------

tables_with_company_id = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "financial_ratios",
    "stock_prices",
    "analysis"
]

for table in tables_with_company_id:

    query = f"""
    SELECT COUNT(*)
    FROM {table}
    WHERE company_id NOT IN (
        SELECT company_id FROM companies
    )
    """

    result = conn.execute(query).fetchone()[0]

    if result > 0:
        add_result(
            "DQ-04",
            "CRITICAL",
            table,
            "FAIL",
            f"{result} invalid company_id records found"
        )
    else:
        add_result(
            "DQ-04",
            "CRITICAL",
            table,
            "PASS",
            "All foreign keys valid"
        )
# -------------------------
# DQ-05 : Balance Sheet Equation
# -------------------------

balance_sheet = pd.read_sql(
    "SELECT * FROM balancesheet",
    conn
)

invalid_balance = balance_sheet[
    (
        balance_sheet["total_liabilities"] +
        balance_sheet["equity"]
    ) != balance_sheet["total_assets"]
]

if len(invalid_balance) > 0:
    add_result(
        "DQ-05",
        "CRITICAL",
        "balancesheet",
        "FAIL",
        f"{len(invalid_balance)} records failed the balance equation"
    )
else:
    add_result(
        "DQ-05",
        "CRITICAL",
        "balancesheet",
        "PASS",
        "Balance sheet equation satisfied."
    )

# -------------------------
# DQ-06 : Positive Sales Check
# -------------------------

profit_loss = pd.read_sql(
    "SELECT * FROM profitandloss",
    conn
)

invalid_sales = profit_loss[
    profit_loss["sales"] <= 0
]

if len(invalid_sales) > 0:
    add_result(
        "DQ-06",
        "CRITICAL",
        "profitandloss",
        "FAIL",
        f"{len(invalid_sales)} records have non-positive sales."
    )
else:
    add_result(
        "DQ-06",
        "CRITICAL",
        "profitandloss",
        "PASS",
        "All sales values are positive."
    )
# -------------------------
# DQ-07 : Duplicate Company-Year Check
# -------------------------

duplicates = profit_loss.groupby(
    ["company_id", "year"]
).size().reset_index(name="count")

duplicates = duplicates[
    duplicates["count"] > 1
]

if len(duplicates) > 0:
    add_result(
        "DQ-07",
        "CRITICAL",
        "profitandloss",
        "FAIL",
        f"{len(duplicates)} duplicate company-year records found."
    )
else:
    add_result(
        "DQ-07",
        "CRITICAL",
        "profitandloss",
        "PASS",
        "No duplicate company-year records."
    )
# -------------------------
# DQ-08 : Positive Stock Price Check
# -------------------------

stock_prices = pd.read_sql(
    "SELECT * FROM stock_prices",
    conn
)

invalid_prices = stock_prices[
    stock_prices["close_price"] <= 0
]

if len(invalid_prices) > 0:
    add_result(
        "DQ-08",
        "CRITICAL",
        "stock_prices",
        "FAIL",
        f"{len(invalid_prices)} records have invalid stock prices."
    )
else:
    add_result(
        "DQ-08",
        "CRITICAL",
        "stock_prices",
        "PASS",
        "All stock prices are positive."
    )


    # Save report
report = pd.DataFrame(validation_results)

report.to_csv(
    "output/validation_failures.csv",
    index=False
)

print(report)

conn.close()