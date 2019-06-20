
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board

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

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        pass

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

print('Peça:  ', '-', t.find_piece(*c), '-')
print('Upper: ', '-', t.find_upper_piece(*c), '-')
print('Right: ', '-', t.find_right_piece(*c), '-')
print('Under: ', '-', t.find_under_piece(*c), '-')
print('Left:  ', '-', t.find_left_piece(*c), '-')
# print(t.territory(*c))


