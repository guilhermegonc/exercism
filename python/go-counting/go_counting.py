class Board:

    def __init__(self, board):
        self.board = board
        self.test = self.find_right_piece(0, 0)

    def __repr__(self):
        return '\n'.join(self.board)

    def territory(self, x, y):
        piece = self.find_piece(x, y)
        if piece[0] in 'BW':
            return NONE
        piece += self.find_upper_piece(x, y)
        piece += self.find_right_piece(x, y)
        piece += self.find_under_piece(x, y)
        piece += self.find_left_piece(x, y)
        piece = piece.strip()

        if piece.strip() in ['WW', 'WWW', 'WWWW']:
            return WHITE
        if piece.strip() in ['BB', 'BBB', 'BBBB']:
            return BLACK
        return NONE
  
    def find_piece(self, x, y):
        return self.board[y][x]

    def find_upper_piece(self, x, y):
        begin = y - 1 if y - 1 >= 0 else 0
        rng = list(range(begin, -1, -1))
        for ind, c in enumerate(self.board[begin::-1]):
            if c[x] != ' ':
                return c[x], rng
        return None, rng

    def find_right_piece(self, x, y):
        rng = list(range(x + 1, 5))
        for c in self.board[y][x + 1:]:
            if c != ' ':
                return c, rng
        return None, rng

    def find_under_piece(self, x, y):
        rng = list(range(y + 1, 5))
        for c in self.board[y + 1:]:
            if c[x] != ' ':
                return c[x], rng
        return None, rng

    def find_left_piece(self, x, y):
        begin = x - 1 if x - 1 >= 0 else 0
        rng = list(range(begin, -1, -1))
        for c in self.board[y][begin::-1]:
            if c != ' ':
                return c, rng
        return None, rng


class BLACK:
    def __init__(self):
        self.BLACK = "Black"


class WHITE:
    def __init__(self):
        self.WHITE = "White"


class NONE:
    def __init__(self):
        self.NONE = None


test =[
    "  B  ",
    " B B ",
    "B W B",
    " W W ",
    "  W  "
]

t = Board(test)
c = (2, 1)
print(t.test)
