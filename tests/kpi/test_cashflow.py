from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
    capital_allocation_pattern,
)


def test_free_cash_flow():
    assert free_cash_flow(100, -30) == 70


def test_cfo_quality_high():
    score, label = cfo_quality_score(120, 100)
    assert score == 1.2
    assert label == "High Quality"


def test_cfo_quality_moderate():
    score, label = cfo_quality_score(70, 100)
    assert label == "Moderate"


def test_cfo_quality_low():
    score, label = cfo_quality_score(30, 100)
    assert label == "Accrual Risk"


def test_cfo_quality_zero_pat():
    score, label = cfo_quality_score(100, 0)
    assert score is None
    assert label is None


def test_capex_intensity():
    value, label = capex_intensity(-50, 1000)
    assert value == 5.0
    assert label == "Moderate"


def test_fcf_conversion():
    assert fcf_conversion_rate(80, 100) == 80.0


def test_fcf_conversion_zero():
    assert fcf_conversion_rate(80, 0) is None


def test_pattern_reinvestor():
    assert capital_allocation_pattern(100, -50, -20) == "Reinvestor"


def test_pattern_growth_debt():
    assert capital_allocation_pattern(-100, -20, 50) == "Growth Funded by Debt"