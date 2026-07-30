import sqlite3

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_assets,
)

conn = sqlite3.connect("database/nifty100.db")
cursor = conn.cursor()

query = """
SELECT
    fr.id,
    p.sales,
    p.operating_profit,
    p.net_profit,
    b.total_assets,
    c.operating_cashflow,
    c.investing_cashflow
FROM financial_ratios fr
JOIN profitandloss p
ON fr.company_id = p.company_id
AND fr.year = p.year
JOIN balancesheet b
ON fr.company_id = b.company_id
AND fr.year = b.year
JOIN cashflow c
ON fr.company_id = c.company_id
AND fr.year = c.year
"""

rows = cursor.execute(query).fetchall()

for row in rows:
    (
        ratio_id,
        sales,
        operating_profit,
        net_profit,
        total_assets,
        operating_cashflow,
        investing_cashflow,
    ) = row

    npm = net_profit_margin(net_profit, sales)
    opm = operating_profit_margin(operating_profit, sales)
    roa = return_on_assets(net_profit, total_assets)
    fcf = operating_cashflow + investing_cashflow

    cursor.execute(
        """
        UPDATE financial_ratios
        SET
            net_profit_margin_pct=?,
            operating_profit_margin_pct=?,
            return_on_assets_pct=?,
            free_cash_flow=?
        WHERE id=?
        """,
        (
            npm,
            opm,
            roa,
            fcf,
            ratio_id,
        ),
    )

conn.commit()
conn.close()

print("Financial ratios updated successfully!")