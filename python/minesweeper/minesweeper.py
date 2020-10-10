def annotate(minefield):
    if invalid_input(minefield):
        raise ValueError('Invalid input')

    scores = []
    for ind, row in enumerate(minefield):
        row = row.replace(' ', '0')
        row = list(row)
        row = [look_neighbors(ind, col, p, minefield) if p.isnumeric() else '*' for col, p in enumerate(row)]
        scores.append(row)

    for ind, row in enumerate(scores):
        minefield[ind] = ''.join([str(c) for c in row])

    return minefield


def invalid_input(lst):
    input_str = ''.join(lst)
    input_str = input_str.replace(' ', '')
    input_str = input_str.replace('*', '')

    set_len = [len(l) for l in lst]
    set_len = set(set_len)

    return input_str != '' or len(set_len) > 1


def look_neighbors(i, j, value, board):
    count = int(value)
    row_lim, col_lim = len(board) - 1, len(board[0]) - 1

    for c in range(j-1, j+2):
        for r in range(i-1, i+2):
            count += 1 if in_limits(r, row_lim, c, col_lim) and board[r][c] == '*' else 0

    return count if count > 0 else ' '


def in_limits(row, max_row, col, max_col):
    return 0 <= row <= max_row and 0 <= col <= max_col
