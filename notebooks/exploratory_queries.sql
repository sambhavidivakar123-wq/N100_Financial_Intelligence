-- Query 1: View all companies
SELECT * FROM companies;

-- Query 2: Count companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- Query 3: Companies by sector
SELECT sector, COUNT(*) AS company_count
FROM companies
GROUP BY sector;

-- Query 4: Profit & Loss data
SELECT company_id, year, sales, net_profit
FROM profitandloss;

-- Query 5: Top companies by sales
SELECT company_id, sales
FROM profitandloss
ORDER BY sales DESC;

-- Query 6: Balance Sheet
SELECT company_id, total_assets, total_liabilities, equity
FROM balancesheet;

-- Query 7: Cash Flow
SELECT company_id, operating_cash_flow
FROM cashflow;

-- Query 8: Financial Ratios
SELECT company_id, pe_ratio, roe
FROM financial_ratios;

-- Query 9: Stock Prices
SELECT company_id, date, close_price
FROM stock_prices
ORDER BY date DESC;

-- Query 10: Analysis Table
SELECT *
FROM analysis;