import pandas as pd
from datetime import datetime
import os

os.makedirs("output", exist_ok=True)

audit = pd.DataFrame({
    "table_name": ["companies"],
    "rows_loaded": [5],
    "rows_rejected": [0],
    "status": ["SUCCESS"],
    "load_time": [datetime.now()]
})

audit.to_csv("output/load_audit.csv", index=False)

print("load_audit.csv generated successfully!")