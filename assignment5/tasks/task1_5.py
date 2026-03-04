def is_valid_course_code(code):
    
    if len(code) != 5 and len(code) != 6:
        return False
    
    letters = code[:-3]   
    digits = code[-3:]    
    
    if not letters.isalpha():
        return False
    if not letters.isupper():
        return False
    
    if not digits.isdigit():
        return False
    
    return True