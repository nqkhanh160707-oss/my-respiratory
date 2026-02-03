def acronym (phrase):
    words = phrase.split()
    acronym_str = ""
    for word in words:
        acronym_str += word[0].upper()
    return acronym_str