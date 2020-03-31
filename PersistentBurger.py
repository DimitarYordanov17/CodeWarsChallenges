def persistence(n):
    counter = 0
    while len(str(n)) > 1:
        digits = [i for i in str(n)]
        n = 5
        counter += 1

    return counter

persistence(125)