def sum_of_intervals(intervals):
    set_sum = set()
    passed = []
    for interval in intervals:
        if interval not in passed:
            elements = list(range(interval[0], interval[1]))
            [set_sum.add(element) for element in elements]
    return len(set_sum)
