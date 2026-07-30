"""
CAGR Engine
Sprint 2 - Day 10
"""

from typing import Optional, Tuple


def calculate_cagr(
    start_value: float,
    end_value: float,
    years: int,
) -> Tuple[Optional[float], str]:
    """
    CAGR = ((End / Start) ** (1 / Years) - 1) * 100

    Returns:
        (value, flag)
    """

    if years <= 0:
        return None, "INVALID_PERIOD"

    if start_value == 0:
        return None, "ZERO_BASE"

    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    cagr = ((end_value / start_value) ** (1 / years) - 1) * 100

    return round(cagr, 2), "NORMAL"

def has_sufficient_years(
    available_years: int,
    required_years: int,
):
    """
    Check whether enough history exists.
    """
    if available_years < required_years:
        return False, "INSUFFICIENT"

    return True, "NORMAL"