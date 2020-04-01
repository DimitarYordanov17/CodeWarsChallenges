def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    return_raised = lambda a: [i ** counter for i, counter in zip([int(x) for x in str(a)], range(1, len(str(a)) + 1))]
    return [x for x in range(a, b + 1) if sum(return_raised(x)) == x]
