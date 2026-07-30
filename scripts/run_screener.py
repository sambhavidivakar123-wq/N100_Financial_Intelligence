import pandas as pd

from src.screener.export import export_screener_results

df = pd.read_excel("data/processed/master_financial_dataset.xlsx")

export_screener_results(df)