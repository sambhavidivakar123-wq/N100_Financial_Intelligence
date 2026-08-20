# N100 Financial Intelligence

A Python-based financial analytics and investment intelligence platform for analyzing company fundamentals, screening stocks, comparing peers, evaluating valuation metrics, analyzing cash flows, generating NLP-based insights, and exposing financial data through a REST API.

## Project Overview

**N100 Financial Intelligence** combines financial data engineering, fundamental analysis, investment screening, financial intelligence, NLP, visualization, and API services into a single modular platform.

The system provides:

* Automated financial data processing and ETL
* SQLite-based financial data storage
* 50+ financial KPIs and ratios
* Configurable stock screening
* Peer comparison and percentile ranking
* Valuation analysis and valuation flags
* Cash Flow Intelligence
* NLP-generated company pros and cons
* Investment radar analysis
* Interactive Streamlit dashboard
* FastAPI REST backend
* Swagger/OpenAPI documentation
* Automated testing with **76/76 tests passing**
* Excel-based analytical reports

> **Current verified dataset:** The processed master financial dataset currently contains 5 companies for the 2024 financial year. The architecture is designed to support a larger Nifty 100 dataset as additional company data becomes available.

---

## Key Features

### 1. Financial Data Pipeline

The project includes an ETL pipeline that converts financial source files into structured analytical datasets.

Supported financial data includes:

* Company information
* Profit and loss statements
* Balance sheets
* Cash flow statements
* Financial ratios
* Stock prices
* Sector information
* Analysis and recommendation data

The processed data is stored and analyzed through a SQLite database.

---

### 2. SQLite Database

The project uses SQLite for structured financial data storage.

The database organizes information into tables for:

* Companies
* Profit and loss
* Balance sheet
* Cash flow
* Financial ratios
* Stock prices
* Sectors
* Analysis and related financial information

Database file:

```text
database/nifty100.db
```

The ETL process also generates load-audit information to support data validation.

---

### 3. Financial Ratio & KPI Engine

The platform calculates **50+ financial KPIs** for fundamental analysis.

Key metrics include:

* Return on Equity (ROE)
* Return on Assets (ROA)
* Return on Capital Employed (ROCE)
* Net Profit Margin
* Operating Profit Margin
* Debt-to-Equity Ratio
* Asset Turnover
* Free Cash Flow
* FCF Yield
* P/E
* P/B
* EV/EBITDA
* Growth metrics
* Profitability metrics
* Leverage metrics
* Efficiency metrics

The ratio engine also handles edge cases and validates calculated financial metrics.

---

### 4. Quality Screener Engine

The Screener Engine identifies companies matching configurable financial criteria.

Available screening presets include:

* Quality Compounder
* Value Pick
* Growth Accelerator
* Dividend Champion
* Debt-Free Blue Chip
* Turnaround Watch

Configuration is maintained through:

```text
config/screener_config.yaml
```

Example command:

```bash
python -m scripts.run_screener
```

Output:

```text
output/screener_output.xlsx
```

---

### 5. Peer Comparison Engine

The Peer Comparison Engine evaluates companies relative to their peers.

Capabilities include:

* Sector-wise comparison
* Fundamental benchmarking
* Percentile ranking
* Relative performance analysis
* Automated Excel report generation
* Conditional formatting

Important comparison metrics include:

* ROE
* ROCE
* Net Profit Margin
* Free Cash Flow
* Asset Turnover
* Debt-to-Equity

Output:

```text
output/peer_comparison.xlsx
```

---

### 6. Valuation Module

The valuation module provides fundamental valuation indicators and identifies potential valuation flags.

Metrics include:

* P/E
* P/B
* EV/EBITDA
* FCF Yield
* Historical median P/E
* Sector-relative P/E
* Valuation flags

Outputs include:

```text
output/valuation_summary.xlsx
output/valuation_flags.csv
```

---

### 7. Cash Flow Intelligence

The Cash Flow Intelligence module evaluates the quality and sustainability of company cash flows.

It analyzes:

* Free Cash Flow
* CFO quality
* CapEx intensity
* Capital allocation patterns
* Potential financial distress indicators

Outputs:

```text
output/cashflow_intelligence.xlsx
output/distress_alerts.csv
```

---

### 8. NLP Pros & Cons Generator

The NLP module extracts financial information from analysis data and generates investor-focused company insights.

The parser processes fields such as:

* Compounded sales growth
* Compounded profit growth
* Stock price CAGR
* ROE
* Ratings
* Recommendations

The Pros & Cons Generator produces structured company-level insights and exports them to:

```text
output/pros_cons_summary.xlsx
```

---

### 9. Investment Radar Analysis

The investment radar module provides visual comparisons of company fundamentals.

It helps identify:

* Strong financial characteristics
* Relative strengths
* Relative weaknesses
* Peer positioning

Run:

```bash
python -m scripts.run_radar
```

---

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring financial intelligence.

Dashboard capabilities include:

* Company overview
* Company profiles
* Stock screening
* Peer comparison
* Financial trends
* Sector analysis
* Valuation insights
* Financial intelligence outputs

The dashboard is organized into modular pages under:

```text
src/dashboard/
```

Run the dashboard using the project's Streamlit entry point:

```bash
streamlit run src/dashboard/app.py
```

---

## FastAPI Backend

The project provides a REST API for accessing company and financial information.

The API is implemented using:

```text
FastAPI
```

API source:

```text
src/api/
```

The backend provides endpoints for accessing financial intelligence and company-related data.

### Swagger / OpenAPI

Once the FastAPI server is running, interactive API documentation is available through the Swagger UI.

Typical local URL:

```text
http://127.0.0.1:8000/docs
```

The OpenAPI specification is automatically generated by FastAPI.

---

## System Architecture

```text
                    Financial Source Files
                           |
                           v
                    +--------------+
                    | ETL Pipeline |
                    +--------------+
                           |
                           v
                    +--------------+
                    | SQLite DB    |
                    | nifty100.db  |
                    +--------------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        KPI Engine     Screener      Peer Engine
             |             |             |
             +-------------+-------------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Valuation     Cash Flow       NLP
          Engine      Intelligence   Insights
             |             |             |
             +-------------+-------------+
                           |
                +----------+----------+
                |                     |
                v                     v
        Streamlit Dashboard      FastAPI API
                                      |
                                      v
                              Swagger / OpenAPI
```

---

## Project Structure

```text
N100_Financial_Intelligence/
|
+-- config/
|   +-- screener_config.yaml
|
+-- data/
|   +-- raw/
|   +-- processed/
|
+-- database/
|   +-- nifty100.db
|
+-- db/
|
+-- notebooks/
|
+-- output/
|   +-- screener_output.xlsx
|   +-- peer_comparison.xlsx
|   +-- valuation_summary.xlsx
|   +-- valuation_flags.csv
|   +-- cashflow_intelligence.xlsx
|   +-- distress_alerts.csv
|   +-- pros_cons_summary.xlsx
|
+-- reports/
|
+-- scripts/
|   +-- run_screener.py
|   +-- run_peer.py
|   +-- run_radar.py
|   +-- run_valuation.py
|   +-- run_cashflow.py
|   +-- data preparation scripts
|
+-- src/
|   +-- analytics/
|   +-- api/
|   +-- dashboard/
|   +-- etl/
|   +-- nlp/
|   +-- screener/
|
+-- tests/
|
+-- .gitignore
+-- pytest.ini
+-- requirements.txt
+-- README.md
```

---

## Technology Stack

### Programming & Data

* Python
* Pandas
* NumPy
* SciPy
* SQL
* SQLite

### Financial Analytics

* Financial ratios
* Fundamental screening
* Peer benchmarking
* Valuation analysis
* Cash-flow analysis
* Financial intelligence

### NLP

* Python-based text parsing
* Regular expressions
* Automated pros and cons generation

### Visualization & Applications

* Streamlit
* Excel reporting
* OpenPyXL
* Radar visualization

### API

* FastAPI
* REST API
* Swagger UI
* OpenAPI

### Testing & Development

* PyTest
* Git
* GitHub
* Virtual environments

---

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd N100_Financial_Intelligence
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run Screener

```bash
python -m scripts.run_screener
```

Generates:

```text
output/screener_output.xlsx
```

### Run Peer Comparison

```bash
python -m scripts.run_peer
```

Generates:

```text
output/peer_comparison.xlsx
```

### Run Valuation

```bash
python -m scripts.run_valuation
```

Generates valuation outputs in:

```text
output/
```

### Run Cash Flow Intelligence

```bash
python -m scripts.run_cashflow
```

Generates:

```text
output/cashflow_intelligence.xlsx
output/distress_alerts.csv
```

### Run Investment Radar

```bash
python -m scripts.run_radar
```

### Run Streamlit Dashboard

```bash
streamlit run src/dashboard/app.py
```

### Run FastAPI

Use the project's FastAPI entry point and then open:

```text
http://127.0.0.1:8000/docs
```

for Swagger/OpenAPI documentation.

---

## Testing

The project uses **PyTest** for automated validation.

Run the complete test suite:

```bash
pytest -v
```

### Verified Result

```text
76 passed
```

**76/76 automated tests passed successfully.**

The test suite validates major project components including:

* Financial ratio calculations
* Edge cases
* Screener functionality
* Screening presets
* Peer comparison
* API functionality
* Financial analytics
* Data processing
* Other core project modules

---

## Generated Outputs

The project generates multiple analytical outputs, including:

```text
output/
|
+-- screener_output.xlsx
+-- peer_comparison.xlsx
+-- valuation_summary.xlsx
+-- valuation_flags.csv
+-- cashflow_intelligence.xlsx
+-- distress_alerts.csv
+-- pros_cons_summary.xlsx
```

These outputs provide structured financial intelligence that can be consumed through Excel, the dashboard, or the API.

---

## Project Status

### Completed

* [x] SQLite Database
* [x] ETL Pipeline
* [x] Financial KPI Engine
* [x] 50+ Financial KPIs
* [x] Screener Engine
* [x] Peer Comparison Engine
* [x] Valuation Module
* [x] Cash Flow Intelligence
* [x] NLP Pros & Cons Generator
* [x] Investment Radar
* [x] Streamlit Dashboard
* [x] FastAPI Backend
* [x] Swagger/OpenAPI Documentation
* [x] Automated Test Suite
* [x] Git repository cleanup
* [x] Python `.gitignore` configuration

### Test Status

**76/76 tests passed**

---

## Future Enhancements

Potential future improvements include:

* Expanding the master dataset to cover the complete target universe
* Integrating live market data
* Automated financial-data refresh
* Machine-learning-based stock scoring
* Portfolio optimization
* Advanced financial forecasting
* Automated PDF tear sheets
* Cloud deployment
* Authentication and API access control
* Scheduled data pipelines

---

## Author

**N100 Financial Intelligence Project**

Built as a financial analytics and investment intelligence platform combining data engineering, financial analysis, NLP, visualization, APIs, and automated testing.
