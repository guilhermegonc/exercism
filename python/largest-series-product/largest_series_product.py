def test_input(series, size):
    if size > len(series) or size < 0:
        raise ValueError('Invalid syntax, check the sample size.')
    for c in series:
        if c.lower() not in '0123456789':
            raise ValueError('Invalid series. Check for not numerals.')


def prod_from_list(text):
    result = 1
    for f in text:
        result *= int(f)
    return result


def largest_product(series, size):
    test_input(series, size)
    max_prod = 0
    for pos in range(0, len(series) - size + 1):
        prod = prod_from_list(series[pos: pos + size])
        if prod > max_prod:
            max_prod = prod
    return max_prod
