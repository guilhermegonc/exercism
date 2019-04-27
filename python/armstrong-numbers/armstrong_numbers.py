def is_armstrong(number):
    value = 0
    factors = str(number)
    power = len(factors)

    for f in factors:
        value += int(f) ** power

    return number == value
