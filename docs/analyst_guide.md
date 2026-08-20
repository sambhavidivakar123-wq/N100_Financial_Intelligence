# N100 Financial Intelligence Platform - Analyst Guide

## Overview

N100 Financial Intelligence is a financial analytics platform designed to evaluate company fundamentals, perform screening, compare peers, generate valuation insights, and expose data through a FastAPI service.

## Core Components

### Data Layer
- companies.xlsx
- profitandloss.xlsx
- balancesheet.xlsx
- cashflow.xlsx
- financial_ratios.xlsx
- analysis.xlsx
- stock_prices.xlsx

### Database
- SQLite
- database/nifty100.db

### Analytics Modules
- Financial Ratio Engine
- Screener Engine
- Peer Comparison Engine
- Valuation Engine
- Cash Flow Intelligence
- NLP Insight Generator
- Clustering Module

## Dashboard

Streamlit dashboard includes:
1. Home
2. Company Profile
3. Screener
4. Peer Comparison
5. Trends
6. Sectors
7. Capital Allocation
8. Reports

## API Endpoints

- /health
- /companies
- /companies/{ticker}
- /companies/{ticker}/pl
- /companies/{ticker}/bs
- /companies/{ticker}/cashflow
- /companies/{ticker}/ratios
- /screener
- /peers
- /portfolio/stats
- /documents
- /sectors
- /valuation

## Outputs

- screener_output.xlsx
- peer_comparison.xlsx
- valuation_summary.xlsx
- cashflow_intelligence.xlsx
- cluster_labels.csv
- portfolio_summary.pdf

## Testing

Run:

```bash
pytest -v
```

All tests must pass before release.

## Author

N100 Financial Intelligence Project