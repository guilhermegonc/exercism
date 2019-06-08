def largest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError('Input error, minimum value is greater than maximum')

    all_factors = tuple(range(max_factor, min_factor - 1, -1))

    palindrome_value = find_max_palindrome(all_factors)
    factors = filter_max_palindrome_factors(palindrome_value, all_factors)

    return palindrome_value, factors


def smallest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError('Input error, minimum value is greater than maximum')

    all_factors = tuple(range(min_factor, max_factor + 1))

    palindrome_value = find_min_palindrome(all_factors)
    factors = filter_min_palindrome_factors(palindrome_value, all_factors)

    return palindrome_value, factors


def find_max_palindrome(values):
    palindrome_value = None
    lower_limit = values[-1] ** 2

    for i in values:
        for j in range(i * values[0], i ** 2 - 1, -i):

            if j < lower_limit:
                break

            if is_palindrome(j):
                palindrome_value = j
                lower_limit = palindrome_value

    return palindrome_value


def find_min_palindrome(values):
    palindrome_value = None
    top_limit = values[-1] ** 2

    for i in values:
        for j in range(i ** 2, i * values[-1] + 1, i):

            if j > top_limit:
                break

            if is_palindrome(j):
                palindrome_value = j
                top_limit = palindrome_value

    return palindrome_value


def filter_max_palindrome_factors(palindrome_value, values):
    factors = []
    for i in values:
        if palindrome_value is None:
            break

        for j in range(i * values[0], i ** 2 - 1, -i):
            if j < palindrome_value:
                break

            if j == palindrome_value:
                factors.append((i, int(j / i)))

    return factors


def filter_min_palindrome_factors(palindrome_value, values):
    factors = []
    for i in values:
        if palindrome_value is None:
            break

        for j in range(i ** 2, i * values[-1] + 1, i):
            if j > palindrome_value:
                break

            if j == palindrome_value:
                factors.append((i, int(j / i)))

    return factors


def is_palindrome(value):
    return str(value) == str(value)[::-1]
