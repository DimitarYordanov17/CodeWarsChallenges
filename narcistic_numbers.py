def narcissistic( value ):
    # Find if an number is narcissistic
    digits = [int(i) for i in str(value)]
    digits_powers = [x ** len(digits) for x in digits]
    if sum(digits_powers) == value:
        return True
    else:
        return False