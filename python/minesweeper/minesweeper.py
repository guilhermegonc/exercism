def annotate(minefield):
    for line, l in enumerate(minefield):
        ans = l.replace(' ', '0')
        ans = list(ans)
        ans = [look_neighbors(row, line, minefield) if p == '*' else p for row, p in enumerate(ans)]
        print(''.join(ans))
    # if invalid_input(minefield):
    #     raise ValueError('Invalid input')
    #
    # for row, m in enumerate(minefield):
    #     pieces = list(m)
    #     for col, p in enumerate(pieces):
    #         score = 0
    #         if pieces[col] != '*':
    #             for i in range(-1, 2):
    #                 for j in range(-1, 2):
    #                     score += 1 if is_mine_next(minefield, row + i, col + j) else 0
    #                 pieces[col] = str(score) if score != 0 else ' '
    #                 minefield[row] = ''.join(pieces)
    #
    # return minefield


def invalid_input(lst):
    input_str = ''.join(lst)
    input_str = input_str.replace(' ', '')
    input_str = input_str.replace('*', '')

    set_len = [len(l) for l in lst]
    set_len = set(set_len)

    return input_str != '' or len(set_len) > 1


def is_mine_next(lst, i, j):
    l_limit, r_limit = len(lst), len(lst[0])
    if 0 <= i < l_limit and 0 <= j < r_limit:
        return lst[i][j] == '*'
    pass


def look_neighbors(i, j, board):
    for r in range(i-1, i+2):
        # print(board[j][r])
        board[j][r] = 1 if 0 <= r >= 2  and board[j][r] != '*' else '*'
    return '*'


bola = ['0*0']
annotate(bola)
