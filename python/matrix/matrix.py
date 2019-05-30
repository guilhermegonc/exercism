class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(s) for s in i.split()] for i in matrix_string.split('\n')]

    def __repr__(self):
        return str(self.matrix)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [c[index - 1] for c in self.matrix]
