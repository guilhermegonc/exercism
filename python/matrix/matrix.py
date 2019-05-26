class Matrix(object):
    def __init__(self, matrix_string):
        matrix = []
        for r in matrix_string.split('\n'):
            try:
                row = list(map(int, r.split(' ')))
                matrix.append(row)
            except ValueError:
                print('Matrix elements must be int.')
        self.matrix = matrix

    def __repr__(self):
        return str(self.matrix)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [c[index - 1] for c in self.matrix]
