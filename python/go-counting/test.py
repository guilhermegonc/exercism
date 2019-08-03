class Board:
    def __init__(self, board):
        self.board = board
        self.max_rows = len(self.board)
        self.max_columns = len(self.board[0])
        for i in board:
            for j in i:
                if j not in 'BW':
                    print(j)

    def __repr__(self):
        return f"{self.board}, rows: {self.max_rows}, columns: {self.max_columns}"

    def territory(self, x, y):
        self.validate_coordinates(x, y)

        if self.find_piece(x, y) != ' ':
            return NONE, set()

        if self.find_neighbors(x, y)[0] in ['BB', 'BBB', 'BBBB']:
            return BLACK, set(self.find_neighbors(x, y)[1])

        if self.find_neighbors(x, y)[0] in ['WW', 'WWW', 'WWWW']:
            return WHITE, set(self.find_neighbors(x, y)[1])

        return NONE, set()

    def territories(self):
        pass

    def validate_coordinates(self, x, y):
        if 0 <= x < self.max_columns and 0 <= y < self.max_rows:
            return
        raise ValueError('Coordinates out of index.')

    def find_piece(self, x, y):
        return self.board[y][x]

    def find_neighbors(self, x, y):
        neighbors = ''
        areas = []

        neighbors += self.find_upper_piece(x, y)[0]
        areas += self.find_upper_piece(x, y)[1]

        neighbors += self.find_right_piece(x, y)[0]
        areas += self.find_right_piece(x, y)[1]

        neighbors += self.find_under_piece(x, y)[0]
        areas += self.find_under_piece(x, y)[1]

        neighbors += self.find_left_piece(x, y)[0]
        areas += self.find_left_piece(x, y)[1]

        return neighbors, areas

    def find_upper_piece(self, x, y):
        bolas = []
        for ind, c in enumerate(self.board[y::-1]):
            # print(f'up-{c[x]}-', x, ind + y)

            if c[x] == 'B':
                return 'B', bolas

            if c[x] == 'W':
                return 'W', bolas

            bolas.append((x, ind + y))
        return '', bolas

    def find_right_piece(self, x, y):
        bolas = []
        for ind, c in enumerate(self.board[y][x:]):
            # print(f'right-{c}-', ind + x, y)

            if c == 'B':
                return 'B', bolas

            if c == 'W':
                return 'W', bolas

            bolas.append((ind + x, y))

        return '', bolas

    def find_under_piece(self, x, y):
        bolas = []
        for ind, c in enumerate(self.board[y:]):
            # print(f'under-{c[x]}-', x, ind + y)

            if c[x] == 'B':
                return 'B', bolas

            if c[x] == 'W':
                return 'W', bolas

            bolas.append((x, ind + y))

        return '', bolas

    def find_left_piece(self, x, y):
        bolas = []
        for ind, c in enumerate(self.board[y][x::-1]):
            # print(f'left-{c}-', ind + x, x)

            if c == 'B':
                return 'B', bolas

            if c == 'W':
                return 'W', bolas

            bolas.append((ind + x, y))

        return '', bolas


class BLACK:
    def __init__(self):
        self.BLACK = "Black"


class WHITE:
    def __init__(self):
        self.WHITE = "White"


class NONE:
    def __init__(self):
        self.NONE = None


test = [
    "  B  ",
    " B B ",
    "B W B",
    " W W "
    "  W  "
]
t = Board(test)
c = (0, 0)
t.find_neighbors(*c)
print(t.territory(*c))
