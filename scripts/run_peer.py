import pandas as pd

from src.analytics.peer import PeerComparison

df = pd.read_excel(
    "data/processed/master_financial_dataset.xlsx"
)

peer = PeerComparison()

result = peer.calculate_percentiles(df)

peer.export_excel(result)

print("Peer comparison exported successfully.")