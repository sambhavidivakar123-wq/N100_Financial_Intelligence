import pandas as pd

from src.screener.engine import ScreenerEngine


def test_quality_compounder():
    df = pd.DataFrame(
        {
            "roe": [20, 10],
            "debt_to_equity": [0.5, 2.0],
            "free_cash_flow": [100, -10],
            "revenue_cagr_5yr": [15, 5],
        }
    )

    engine = ScreenerEngine()

    result = engine.apply_filters(df, "quality_compounder")

    assert len(result) == 1
    assert result.iloc[0]["roe"] == 20
def test_available_presets():
    engine = ScreenerEngine()

    presets = engine.available_presets()

    assert "quality_compounder" in presets
    assert "value_pick" in presets
    assert "growth_accelerator" in presets
    assert "dividend_champion" in presets
    assert "debt_free_blue_chip" in presets
    assert "turnaround_watch" in presets


def test_unknown_preset():
    import pandas as pd

    df = pd.DataFrame({"roe": [10, 20]})

    engine = ScreenerEngine()

    result = engine.apply_filters(df, "unknown_preset")

    assert len(result) == 2
