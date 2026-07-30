import pandas as pd

from src.analytics.radar import generate_radar_charts
from src.screener.engine import ScreenerEngine

df = pd.read_excel("data/processed/master_financial_dataset.xlsx")

engine = ScreenerEngine()

# Add the composite score before generating charts
df = engine.add_composite_score(df)

generate_radar_charts(df)

print("Radar charts generated successfully.")