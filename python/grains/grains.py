def on_square(integer_number):
    validate_chessboard(integer_number)
    return 2 ** (integer_number - 1)


def total_after(integer_number):
    return on_square(integer_number) * 2 - 1


def validate_chessboard(integer_number):
    if 1 <= integer_number <= 64:
        return
    raise ValueError('This number is out of range the chessboard.')
