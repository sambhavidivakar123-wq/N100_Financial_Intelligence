from fastapi import APIRouter, HTTPException
import pandas as pd
import yaml

router = APIRouter()

MASTER_FILE = "data/processed/master_financial_dataset.xlsx"
CONFIG_FILE = "config/screener_config.yaml"


@router.get("/screener")
def get_screener():
    return {
        "message": "Screener endpoint working",
        "presets": [
            "quality_compounder",
            "value_pick",
            "growth_accelerator",
            "dividend_champion",
            "debt_free_blue_chip",
            "turnaround_watch",
        ],
    }


@router.get("/screener/{preset}")
def run_screener(preset: str):
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}

        if preset not in config:
            raise HTTPException(
                status_code=404,
                detail=f"Screener preset '{preset}' not found",
            )

        df = pd.read_excel(MASTER_FILE)

        filters = config[preset]
        result = df.copy()

        column_map = {
            "roe_min": "roe",
            "debt_to_equity_max": "debt_to_equity",
            "free_cash_flow_min": "free_cash_flow",
            "revenue_cagr_5yr_min": "revenue_cagr_5yr",
        }

        for rule, threshold in filters.items():
            column = column_map.get(rule)

            if column and column in result.columns:
                if rule.endswith("_min"):
                    result = result[result[column] >= threshold]
                elif rule.endswith("_max"):
                    result = result[result[column] <= threshold]

        return {
            "preset": preset,
            "filters": filters,
            "count": len(result),
            "results": result.fillna("").to_dict(orient="records"),
        }

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Required project file not found: {exc.filename}",
        )
