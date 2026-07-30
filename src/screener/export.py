from pathlib import Path

import pandas as pd

from src.screener.engine import ScreenerEngine


def export_screener_results(
    df: pd.DataFrame,
    output_file="output/screener_output.xlsx",
):
    engine = ScreenerEngine()

    Path("output").mkdir(exist_ok=True)

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

        for preset in engine.available_presets():

            result = engine.apply_filters(df, preset)

            result.to_excel(
                writer,
                sheet_name=preset[:31],  # Excel sheet names max 31 chars
                index=False,
            )

    print(f"Saved: {output_file}")