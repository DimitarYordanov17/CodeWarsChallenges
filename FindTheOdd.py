def find_it(seq):
    integers = [x for x in seq if seq.count(x) % 2 == 1]
    return integers[0]



