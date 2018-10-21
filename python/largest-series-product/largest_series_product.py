def largest_product(series, size):
    if invalid_test_input(series, size):
        raise ValueError('Invalid series or size input.')

    max_prod = 0
    for pos in range(len(series) - size + 1):
        if prod_from_list(series[pos: pos + size]) > max_prod:
            max_prod = prod_from_list(series[pos: pos + size])

    return max_prod


def invalid_test_input(series, size):
    return size < 0 or size > len(series) or (len(series) > 0 and not series.isdigit())


def prod_from_list(text):
    result = 1
    for f in text:
        result *= int(f)
    return result
