import os
import pandas as pd


def test_companies_file_exists():
    assert os.path.exists("data/raw/companies.xlsx")


def test_companies_not_empty():
    df = pd.read_excel("data/raw/companies.xlsx")
    assert len(df) > 0


def test_companies_required_columns():
    df = pd.read_excel("data/raw/companies.xlsx")

    expected_columns = [
        "company_id",
        "ticker",
        "company_name",
        "sector"
    ]

    for column in expected_columns:
        assert column in df.columns


def test_company_count():
    df = pd.read_excel("data/raw/companies.xlsx")
    assert len(df) == 5