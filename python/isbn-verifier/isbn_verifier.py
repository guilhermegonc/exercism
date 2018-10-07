from re import search


def verify(isbn):
    isbn = list(isbn.replace('-', ''))

    if invalid_isbn_number(isbn):
        return False
    return (multiply_isbn_terms(isbn[:-1]) + get_last_term(isbn)) % 11 == 0


def invalid_isbn_number(text):
    if len(text) != 10:
        return True

    for n in text[:-2]:
        if search(r'[0-9]', n) is None:
            return True
    pass


def get_last_term(text):
    value = text[-1]

    if value in 'Xx':
        return 10

    if search(r'[0-9]', value) is None:
        return False
    return int(value)


def multiply_isbn_terms(isbn):
    product = 0

    for pos, n in enumerate(isbn[::-1]):
        product += ((pos + 2) * int(n))
    return product
