def classify(number):
    if number <= 0:
        raise ValueError('Invalid input.')
    total = sum_of_factors(number)

    if total < number or number == 1:
        return 'deficient'
    if total > number:
        return 'abundant'
    if total == number:
        return 'perfect'


def sum_of_factors(number):
    total, div, limit = 1, 2, number

    while div < limit:
        if number % div == 0 and number / div != div:
            total += (div + number / div)
        elif number % div == 0:
            total += div
        limit = number / div
        div += 1
    return total
