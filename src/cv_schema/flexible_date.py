from datetime import datetime


def parse_flexible_date(value: str, default: str = "1970-01-01") -> datetime:
    if not value:
        return datetime.fromisoformat(default)

    if isinstance(value, datetime):
        return value

    value_str = str(value).strip()

    if value_str.lower() == "present":
        return datetime.now()

    try:
        return datetime.fromisoformat(value_str)
    except ValueError:
        pass

    try:
        return datetime.strptime(value_str, "%Y-%m")
    except ValueError:
        pass

    try:
        return datetime.strptime(value_str, "%Y")
    except ValueError:
        pass

    raise ValueError(f"Unsupported date format: {value_str}")
