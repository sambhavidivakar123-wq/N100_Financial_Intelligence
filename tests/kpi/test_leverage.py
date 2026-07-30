from src.analytics.ratios import (
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    interest_warning_flag,
    net_debt,
)


def test_debt_to_equity():
    assert debt_to_equity(100, 100, 100) == 0.5


def test_debt_free():
    assert debt_to_equity(0, 100, 100) == 0.0


def test_negative_equity():
    assert debt_to_equity(100, -50, -100) is None


def test_interest_coverage():
    assert interest_coverage_ratio(100, 20, 20) == 6.0


def test_interest_zero():
    assert interest_coverage_ratio(100, 20, 0) is None


def test_icr_label():
    assert icr_label(0) == "Debt Free"


def test_interest_warning():
    assert interest_warning_flag(1.2) is True


def test_high_leverage():
    assert high_leverage_flag(6.0, "Information Technology") is True


def test_high_leverage_financials():
    assert high_leverage_flag(8.0, "Financials") is False


def test_net_debt():
    assert net_debt(1000, 300) == 700