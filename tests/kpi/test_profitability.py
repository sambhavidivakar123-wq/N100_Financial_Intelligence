from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
)


def test_net_profit_margin():
    assert net_profit_margin(20, 100) == 20.0


def test_zero_sales():
    assert net_profit_margin(20, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(30, 100) == 30.0


def test_roe():
    assert return_on_equity(50, 100, 100) == 25.0


def test_negative_equity():
    assert return_on_equity(50, -100, 50) is None


def test_roce():
    assert return_on_capital_employed(50, 100, 100, 50) == 20.0


def test_roa():
    assert return_on_assets(40, 200) == 20.0


def test_zero_assets():
    assert return_on_assets(40, 0) is None