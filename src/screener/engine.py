import pandas as pd
import yaml


class ScreenerEngine:
    def __init__(self, config_path="config/screener_config.yaml"):
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def available_presets(self):
        return list(self.config.keys())

    def _normalize(self, series: pd.Series) -> pd.Series:
        """Normalize values to a 0–100 score using P10/P90 winsorization."""
        series = series.fillna(series.median())

        p10 = series.quantile(0.10)
        p90 = series.quantile(0.90)

        series = series.clip(lower=p10, upper=p90)

        if p90 == p10:
            return pd.Series(50, index=series.index)

        return ((series - p10) / (p90 - p10)) * 100

    def add_composite_score(self, df: pd.DataFrame):
        result = df.copy()

        weights = {
            "roe": 0.15,
            "roce": 0.10,
            "net_profit_margin": 0.10,
            "free_cash_flow": 0.15,
            "operating_cashflow": 0.15,
            "sales": 0.10,
            "net_profit": 0.10,
            "asset_turnover": 0.05,
        }

        score = pd.Series(0.0, index=result.index)
        total_weight = 0

        for column, weight in weights.items():
            if column in result.columns:
                score += self._normalize(result[column]) * weight
                total_weight += weight

        if "debt_to_equity" in result.columns:
            score += (100 - self._normalize(result["debt_to_equity"])) * 0.10
            total_weight += 0.10

        if total_weight > 0:
            score = score / total_weight

        result["composite_quality_score"] = score.round(2)

        return result

    def apply_filters(self, df: pd.DataFrame, preset: str):
        filters = self.config.get(preset, {})
        result = df.copy()

        if (
            "roe_min" in filters
            and "roe" in result.columns
        ):
            result = result[result["roe"] >= filters["roe_min"]]

        if (
            "debt_to_equity_max" in filters
            and "debt_to_equity" in result.columns
        ):
            result = result[
                result["debt_to_equity"]
                <= filters["debt_to_equity_max"]
            ]

        if (
            "free_cash_flow_min" in filters
            and "free_cash_flow" in result.columns
        ):
            result = result[
                result["free_cash_flow"]
                >= filters["free_cash_flow_min"]
            ]

        if (
            "revenue_cagr_5yr_min" in filters
            and "revenue_cagr_5yr" in result.columns
        ):
            result = result[
                result["revenue_cagr_5yr"]
                >= filters["revenue_cagr_5yr_min"]
            ]

        result = self.add_composite_score(result)

        result = result.sort_values(
            "composite_quality_score",
            ascending=False,
        )

        return result.reset_index(drop=True)