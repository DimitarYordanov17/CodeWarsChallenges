def is_prime(number):
    # Not working for now
    number = int(number)
    divisors = [2, 3, 4, 5]

    counter = 0
    for divisor in divisors:
        if number % divisor == 0 and divisor != number:
            counter += 1
            break

    if counter == 1 or number <= 1:
        return False
    elif number > 0:
        return True

