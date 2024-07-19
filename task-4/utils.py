import re

phone_len = 9


def normalize_phone(num: str) -> str:
    normalized = ''
    trimmed = ''.join(re.findall(r"\d+", num))
    if len(trimmed) >= phone_len:
        normalized = f"+380{trimmed[len(trimmed) - phone_len:]}"

    return normalized
