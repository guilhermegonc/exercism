def on_square(integer_number):
    if integer_number not in range(1, 65):
        raise ValueError('This number is out of the range of the chessboard.')
    return 2 ** (integer_number - 1)


def total_after(integer_number):
    return on_square(integer_number) * 2 - 1
