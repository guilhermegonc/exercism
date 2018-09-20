def classify(number):
    validate_input(number)
    s = define_sum_of_factors(number)
    if s == number and number != 1:
        return 'perfect'
    elif s > number:
        return 'abundant'
    else:
        return 'deficient'


def validate_input(number):
    if number <= 0:
        raise ValueError('Invalid input.')
    pass


def define_sum_of_factors(number):
    s, div, limit = 1, 2, number
    while True:
        if div >= limit:
            break
        elif number % div == 0:
            s += div
            if number / div != div:
                s += number / div
        limit = number / div
        div += 1
    return s
