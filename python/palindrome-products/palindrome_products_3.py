def smallest_palindrome(max_factor, min_factor):
    test_input_validity(max_factor, min_factor)

    criteria, i = max_factor ** 2, min_factor ** 2
    while i <= criteria:
        if is_palindrome(i) and len(find_factors(i, max_factor, min_factor)) > 0:
            return i, find_factors(i, max_factor, min_factor)
        i += 1
    return None, []


def largest_palindrome(max_factor, min_factor):
    test_input_validity(max_factor, min_factor)

    criteria, i = min_factor ** 2, max_factor ** 2
    while i >= criteria:
        if is_palindrome(i) and len(find_factors(i, max_factor, min_factor)) > 0:
            return i, find_factors(i, max_factor, min_factor)
        i -= 1
    return None, []


def test_input_validity(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError('Input error, minimum value is greater than maximum')
    return


def find_factors(value, max_factor, min_factor):
    return [(i, int(value/i)) for i in range(min_factor, int(value ** 0.5 + 1))
            if value % i == 0 and max_factor >= value/i >= min_factor]


def is_palindrome(number):
    return str(number) == str(number)[::-1]


print(largest_palindrome(9999, 1000))
