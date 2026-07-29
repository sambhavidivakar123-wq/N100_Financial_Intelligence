import re

def normalize_ticker(ticker):
    """
    Convert ticker to uppercase and remove extra spaces.
    Example: ' tcs ' -> 'TCS'
    """
    if ticker is None:
        return None

    return str(ticker).strip().upper()


def normalize_year(year):
    """
    Convert year to integer.
    Example: '2024' -> 2024
    """
    try:
        return int(year)
    except (ValueError, TypeError):
        return None


import re

def normalize_text(text):
    """
    Remove extra spaces and convert text to uppercase.
    """
    if text is None:
        return None

    text = str(text).strip()
    text = re.sub(r"\s+", " ", text)
    return text.upper()