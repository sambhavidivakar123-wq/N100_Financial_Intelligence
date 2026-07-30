"""
Cash Flow KPI Engine
Sprint 2 - Day 11
"""

from typing import Optional


def free_cash_flow(
    operating_activity: float,
    investing_activity: float,
) -> float:
    """
    Free Cash Flow = CFO + Investing Activity
    (Investing activity is usually negative.)
    """
    return operating_activity + investing_activity


def cfo_quality_score(
    cfo: float,
    pat: float,
) -> tuple[Optional[float], Optional[str]]:
    """
    CFO / PAT
    """
    if pat == 0:
        return None, None

    score = round(cfo / pat, 2)

    if score > 1.0:
        label = "High Quality"
    elif score >= 0.5:
        label = "Moderate"
    else:
        label = "Accrual Risk"

    return score, label


def capex_intensity(
    investing_activity: float,
    sales: float,
) -> tuple[Optional[float], Optional[str]]:
    """
    CapEx Intensity = abs(CFI) / Sales × 100
    """
    if sales == 0:
        return None, None

    value = round(abs(investing_activity) / sales * 100, 2)

    if value < 3:
        label = "Asset Light"
    elif value <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return value, label


def fcf_conversion_rate(
    free_cash_flow: float,
    operating_profit: float,
) -> Optional[float]:
    """
    FCF / Operating Profit × 100
    """
    if operating_profit == 0:
        return None

    return round((free_cash_flow / operating_profit) * 100, 2)


def capital_allocation_pattern(
    cfo: float,
    cfi: float,
    cff: float,
    cfo_pat_ratio: Optional[float] = None,
) -> str:
    """
    Classify cash flow pattern.
    """

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-",
    )

    if signs == ("+", "-", "-"):
        if cfo_pat_ratio is not None and cfo_pat_ratio > 1:
            return "Shareholder Returns"
        return "Reinvestor"

    if signs == ("+", "+", "-"):
        return "Liquidating Assets"

    if signs == ("-", "+", "+"):
        return "Distress Signal"

    if signs == ("-", "-", "+"):
        return "Growth Funded by Debt"

    if signs == ("+", "+", "+"):
        return "Cash Accumulator"

    if signs == ("-", "-", "-"):
        return "Pre-Revenue"

    if signs == ("+", "-", "+"):
        return "Mixed"

    return "Other"