# N100 Financial Intelligence Platform Architecture

```mermaid
flowchart LR

    subgraph Data["Data Sources"]
        A1[companies.xlsx]
        A2[profitandloss.xlsx]
        A3[balancesheet.xlsx]
        A4[cashflow.xlsx]
        A5[financial_ratios.xlsx]
        A6[analysis.xlsx]
        A7[stock_prices.xlsx]
    end

    subgraph ETL["ETL Layer"]
        B1[Loader]
        B2[Validator]
        B3[Normalizer]
    end

    subgraph DB["Storage Layer"]
        C[(SQLite<br/>nifty100.db)]
    end

    subgraph Analytics["Analytics Engine"]
        D1[Financial Ratios]
        D2[Screener Engine]
        D3[Peer Comparison]
        D4[Valuation Engine]
        D5[Cash Flow Intelligence]
        D6[NLP Insights]
        D7[Clustering Module]
    end

    subgraph Outputs["Output Files"]
        O1[screener_output.xlsx]
        O2[peer_comparison.xlsx]
        O3[valuation_summary.xlsx]
        O4[cashflow_intelligence.xlsx]
        O5[pros_cons_summary.xlsx]
        O6[cluster_labels.csv]
    end

    subgraph Dashboard["Streamlit Dashboard"]
        S1[Home]
        S2[Company Profile]
        S3[Screener]
        S4[Peers]
        S5[Trends]
        S6[Sectors]
        S7[Capital Allocation]
        S8[Reports]
    end

    subgraph API["FastAPI Backend"]
        F1[/health]
        F2[/companies]
        F3[/screener]
        F4[/peers]
        F5[/valuation]
        F6[/portfolio]
        F7[/documents]
        F8[/sectors]
    end

    subgraph Reports["PDF Reports"]
        R1[Company Tearsheets]
        R2[Sector Reports]
        R3[Portfolio Summary]
    end

    Data --> ETL
    ETL --> DB

    DB --> D1
    DB --> D2
    DB --> D3
    DB --> D4
    DB --> D5
    DB --> D6
    DB --> D7

    D1 --> Outputs
    D2 --> Outputs
    D3 --> Outputs
    D4 --> Outputs
    D5 --> Outputs
    D6 --> Outputs
    D7 --> Outputs

    DB --> Dashboard
    DB --> API

    D4 --> Reports
    D5 --> Reports
    D6 --> Reports
```