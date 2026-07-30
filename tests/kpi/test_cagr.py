from src.analytics.cagr import (
    calculate_cagr,
    has_sufficient_years,
)


def test_normal_cagr():
    value, flag = calculate_cagr(100, 200, 5)
    assert flag == "NORMAL"
    assert round(value, 2) == 14.87


def test_turnaround():
    value, flag = calculate_cagr(-100, 200, 5)
    assert value is None
    assert flag == "TURNAROUND"


def test_decline_to_loss():
    value, flag = calculate_cagr(100, -50, 5)
    assert value is None
    assert flag == "DECLINE_TO_LOSS"


def test_both_negative():
    value, flag = calculate_cagr(-100, -50, 5)
    assert value is None
    assert flag == "BOTH_NEGATIVE"


def test_zero_base():
    value, flag = calculate_cagr(0, 100, 5)
    assert value is None
    assert flag == "ZERO_BASE"


def test_insufficient():
    ok, flag = has_sufficient_years(3, 5)
    assert ok is False
    assert flag == "INSUFFICIENT"


def test_sufficient():
    ok, flag = has_sufficient_years(5, 5)
    assert ok is True
    assert flag == "NORMAL"


def test_invalid_period():
    value, flag = calculate_cagr(100, 200, 0)
    assert value is None
    assert flag == "INVALID_PERIOD"


def test_same_values():
    value, flag = calculate_cagr(100, 100, 5)
    assert value == 0.0
    assert flag == "NORMAL"


def test_positive_growth():
    value, flag = calculate_cagr(50, 100, 3)
    assert flag == "NORMAL"
    assert value > 0