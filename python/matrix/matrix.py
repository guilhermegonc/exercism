class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.number_of_rows = len(self.matrix_string.split('\n'))

    def __repr__(self):
        return str(self.matrix_string)

    def row(self, index):
        string_list = self.matrix_string.split('\n')[index - 1].split()
        return [int(i) for i in string_list]

    def column(self, index):
        return [self.row(i + 1)[index - 1] for i in range(self.number_of_rows)]
