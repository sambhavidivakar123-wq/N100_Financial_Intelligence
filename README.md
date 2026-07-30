# N100 Financial Intelligence

## Project Overview

N100 Financial Intelligence is a financial analytics and investment intelligence system designed to analyze company fundamentals, compare peers, screen quality companies, and generate investor-focused insights from financial data.

The project automates the process of:

* Financial data preparation
* Ratio analysis
* Fundamental screening
* Peer comparison
* Investment radar visualization
* Excel-based reporting

---

## Key Features

### 1. Financial Data Pipeline

The project processes company financial information and prepares structured datasets for analysis.

Implemented modules:

* Financial dataset creation
* Profit and loss data generation
* Financial ratio calculation
* Database validation

---

## 2. Financial Ratio Analysis

The system calculates important fundamental metrics including:

* Return on Equity (ROE)
* Return on Capital Employed (ROCE)
* Net Profit Margin
* Free Cash Flow
* Asset Turnover
* Debt to Equity Ratio

These metrics are used for company evaluation and comparison.

---

## 3. Quality Screener Engine

The Screener Engine identifies financially strong companies based on predefined investment criteria.

Features:

* Configurable screening rules
* Multiple screening presets
* Automated filtering
* Excel output generation

Output:

```
output/screener_output.xlsx
```

---

## 4. Peer Comparison Analysis

The Peer Comparison module evaluates companies relative to their sector peers.

Capabilities:

* Sector-wise comparison
* Percentile ranking
* Fundamental benchmarking
* Automated Excel reporting

Metrics compared:

* ROE
* ROCE
* Net Profit Margin
* Free Cash Flow
* Asset Turnover
* Debt to Equity

Output:

```
output/peer_comparison.xlsx
```

The Excel report includes conditional formatting:

* Green → Strong relative performance
* Yellow → Average performance
* Red → Weak relative performance

---

## 5. Investment Radar

The project generates visual comparisons to highlight company strengths and weaknesses.

Radar analysis helps identify:

* Strong fundamentals
* Competitive advantages
* Relative ranking among peers

---

## Project Structure

```
N100_Financial_Intelligence/

├── config/
│   └── Screening configurations

├── data/
│   └── Financial datasets

├── database/
│   └── Database files

├── notebooks/
│   └── Analysis notebooks

├── output/
│   ├── screener_output.xlsx
│   └── peer_comparison.xlsx

├── reports/
│   └── Generated reports

├── scripts/
│   ├── run_screener.py
│   ├── run_peer.py
│   ├── run_radar.py
│   └── data preparation scripts

├── src/
│   └── Analytics modules

└── tests/
    └── Unit tests
```

---

## Installation

Create and activate virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

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

```
output/screener_output.xlsx
```

---

### Run Peer Comparison

```bash
python -m scripts.run_peer
```

Generates:

```
output/peer_comparison.xlsx
```

---

### Run Investment Radar

```bash
python -m scripts.run_radar
```

---

## Testing

The project uses pytest for validation.

Run:

```bash
pytest tests/screener/ -v
```

Test results:

```
3 passed
```

Validated:

* Quality compounder screening
* Available presets
* Unknown preset handling

---

## Technologies Used

* Python
* Pandas
* NumPy
* OpenPyXL
* PyTest
* Excel Reporting
* SQLite

---

## Sprint 3 Completion Status

Completed:

✅ Screener Engine
✅ Unit Testing
✅ Peer Comparison Engine
✅ Percentile Ranking
✅ Excel Report Generation
✅ Conditional Formatting
✅ Investment Radar Charts

---

## Future Enhancements

Possible improvements:

* Live market data integration
* Machine learning based stock scoring
* Portfolio optimization
* Web dashboard deployment
* Automated financial updates

---

## Author

N100 Financial Intelligence Project
