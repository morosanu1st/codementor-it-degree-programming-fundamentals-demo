"""Solutions for lesson 07 - error handling."""


def safe_int(text, default=0):
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_port(text):
    try:
        port = int(text)
    except (ValueError, TypeError):
        raise ValueError(f"not a number: {text!r}") from None
    if not 1 <= port <= 65535:
        raise ValueError(f"port out of range: {port}")
    return port
