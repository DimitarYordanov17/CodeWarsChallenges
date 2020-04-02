import re


def domain_name(url):
    pattern = re.compile(r'(www)?\.?([a-zA-Z0-9-]+)\.(([a-zA-Z]+\.?)+)')
    matches = pattern.findall(url)
    return matches[0][1]
