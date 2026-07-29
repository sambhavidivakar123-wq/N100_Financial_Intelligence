from src.etl.normaliser import (
    normalize_ticker,
    normalize_year,
    normalize_text,
)


def test_normalize_ticker_uppercase():
    assert normalize_ticker("tcs") == "TCS"


def test_normalize_ticker_spaces():
    assert normalize_ticker("  infy  ") == "INFY"


def test_normalize_ticker_already_clean():
    assert normalize_ticker("RELIANCE") == "RELIANCE"


def test_normalize_year_integer():
    assert normalize_year(2024) == 2024


def test_normalize_year_string():
    assert normalize_year("2024") == 2024


def test_normalize_text_upper():
    assert normalize_text("banking") == "BANKING"


def test_normalize_text_spaces():
    assert normalize_text("  finance  ") == "FINANCE"


def test_normalize_ticker_mixed_case():
    assert normalize_ticker("ReLiAnCe") == "RELIANCE"


def test_normalize_ticker_empty():
    assert normalize_ticker("") == ""


def test_normalize_text_empty():
    assert normalize_text("") == ""