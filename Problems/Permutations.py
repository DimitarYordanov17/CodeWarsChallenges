import itertools
def permutations(string):
    if len(string) == 1:
        return [string]
    all = list(itertools.permutations(string, len(string)))
    return {"".join(i) for i in all}
