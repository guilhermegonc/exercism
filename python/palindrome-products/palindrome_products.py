def smallest_palindrome(max_factor, min_factor):
    test_input_validity(max_factor, min_factor)

    palindrome = None
    for i in range(min_factor, max_factor):
        if palindrome is not None and i * min_factor >= palindrome:
            break

        for j in range(min_factor, i + 1):
            if (palindrome is None or i * j <= palindrome) and is_palindrome(i * j):
                palindrome = i * j
                break

    return palindrome, find_factors(palindrome, max_factor, min_factor)


def largest_palindrome(max_factor, min_factor):
    test_input_validity(max_factor, min_factor)

    palindrome = None
    for i in range(max_factor, min_factor - 1, -1):
        if palindrome is not None and i * max_factor <= palindrome:
            break

        for j in range(max_factor, i - 1, -1):
            if (palindrome is None or i * j >= palindrome) and is_palindrome(i * j):
                palindrome = i * j
                break

    return palindrome, find_factors(palindrome, max_factor, min_factor)


def test_input_validity(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError('Input error, minimum value is greater than maximum')
    return


def find_factors(value, max_factor, min_factor):
    if value is None:
        return []
    return [(i, int(value/i)) for i in range(min_factor, int(value ** 0.5 + 1))
            if value % i == 0 and max_factor >= value/i >= min_factor]


def is_palindrome(number):
    return str(number) == str(number)[::-1]
