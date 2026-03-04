import re

def hide_phone_numbers(text):
    pattern = r"\+84\d+|\b\d{10}\b"
    result = re.sub(pattern, "[REDACTED]", text)
    return result