def maskify(cc):
    if len(cc) > 4:
        return ("#" * (len(cc) - 4)) + cc[len(cc) - 4:len(cc)]
    elif len(cc) <= 4:
        return cc


