import sqlite3
import logging
import os

os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="output/ratio_edge_cases.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

conn = sqlite3.connect("database/nifty100.db")
cursor = conn.cursor()

query = """
SELECT
    company_id,
    year,
    sales,
    net_profit
FROM profitandloss
"""

rows = cursor.execute(query).fetchall()

issues = 0

for company_id, year, sales, net_profit in rows:

    if sales == 0:
        logging.warning(
            f"Company {company_id} ({year}) - Sales is zero."
        )
        issues += 1

    if net_profit is None:
        logging.warning(
            f"Company {company_id} ({year}) - Net Profit missing."
        )
        issues += 1

print(f"Validation complete. {issues} issue(s) logged.")

conn.close()