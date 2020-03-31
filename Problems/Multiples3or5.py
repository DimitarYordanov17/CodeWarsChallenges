def solution(number):
    multiples3 = list(filter(lambda a: a % 3 == 0, list(range(number))))
    multiples5 = list(filter(lambda a: a % 5 == 0, list(range(number))))

    return sum(set(multiples3 + multiples5))

print(solution(10))
