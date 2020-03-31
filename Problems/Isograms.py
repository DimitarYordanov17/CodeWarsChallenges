def is_isogram(string):
    string = string.lower()
    if len(set(string)) == len(string) and string.isalpha() or len(string) == 0:
        return True
    else:
        return False

