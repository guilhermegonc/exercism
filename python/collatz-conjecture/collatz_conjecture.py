def steps(number):
    test_input(number)

    counter = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        counter += 1
    return counter


def test_input(number):
    if not(isinstance(number, int)) or number <= 0:
        raise ValueError('Invalid input. Number must be a positive integer.')
    return
