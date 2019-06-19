
class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.areas = {"B": BLACK, "W": WHITE, None: NONE}

    def __repr__(self):
        return '\n'.join(self.board)

    def territory(self, x, y):
        return self.areas[self.find_piece(x, y)]

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

    def find_left_piece(self, x, y):
        for c in self.board[y][x - 1::-1]:
            if c != ' ':
                return c
        return None

    def find_right_piece(self, x, y):
        for c in self.board[y][x:]:
            if c != ' ':
                return c
        return None

    def find_upper_piece(self, x, y):
        for c in self.board[y - 1::-1]:
            if c[x] != ' ':
                return c[x]
        return None

    def find_under_piece(self, x, y):
        for c in self.board[y:]:
            if c[x] != ' ':
                return c[x]
        return None


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
c = (2, 0)

# print('Peça:  ', '-', t.find_piece(*c), '-')
# print('Left:  ', '-', t.find_left_piece(*c), '-')
# print('Right: ', '-', t.find_right_piece(*c), '-')
# print('Upper: ', '-', t.find_upper_piece(*c), '-')
# print('Under: ', '-', t.find_under_piece(*c), '-')

print(t.territory(*c))
