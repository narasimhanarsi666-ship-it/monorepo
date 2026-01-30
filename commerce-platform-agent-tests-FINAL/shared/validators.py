def require_fields(data, fields):
    missing = [f for f in fields if f not in data]
    if missing:
        return False, missing
    return True, []

def is_positive_number(value):
    try:
        return float(value) > 0
    except Exception:
        return False
