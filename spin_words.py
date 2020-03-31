# Reverse every word which has length more than 5
def spin_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) >= 5:
            new_words.append(word[::-1])
        else:
            new_words.append(word)
    new_words_string = " ".join(new_words)
    return new_words_string