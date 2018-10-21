def verify(isbn):
    isbn = isbn.replace('-', '')

    if valid_isbn_format(isbn):
        return (multiply_isbn_terms(isbn[:-1]) + get_last_term(isbn)) % 11 == 0
    return False


def valid_isbn_format(text):
    if len(text) != 10:  # Verify ISBN length
        return False

    if not text[:-1].isdigit():
        return False
    return True


def multiply_isbn_terms(isbn):
    product = 0

    for pos, n in enumerate(isbn[::-1]):
        product += ((pos + 2) * int(n))
    return product


def get_last_term(text):
    value = text[-1].upper()

    if value == 'X':
        return 10

    if not value.isdigit():
        return False
    return int(value)
