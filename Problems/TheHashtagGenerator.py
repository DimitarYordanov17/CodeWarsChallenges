def generate_hashtag(string):

    if len(string) == 0:
        return False
    
    while "  " in string:
        string = string.replace("  ", " ")
        
    
    
    text = "".join([i.strip()[0].upper() + i.strip()[1:] for i in string.split()])
    text = [i for i in text]
    text.insert(0, "#")
    text = "".join(text)
    
    if len (text) > 140:
        return False
    else:
        return text
