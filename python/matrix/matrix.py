class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.row_split = self.matrix_string.split('\n')

    def __repr__(self):
        return str(self.matrix_string)

    def row(self, index):
        selected_row = self.row_split[index - 1]
        return [int(i) for i in selected_row.split()]

    def column(self, index):
        return [self.row(i)[index - 1] for i in range(1, len(self.row_split) + 1)]
