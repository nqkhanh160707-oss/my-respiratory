import re

def is_valid_hex_color(color):
    pattern = "^#[0-9A-Fa-f]{6}$"
    
    if re.match(pattern, color):
        return True
    else:
        return False