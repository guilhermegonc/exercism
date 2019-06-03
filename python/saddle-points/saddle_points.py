class Matrix:

    def __init__(self, row_lists):
        self.rows = row_lists
        self.columns = self.split_row_in_columns()
        self.positions = self.map_elements_position()

    def split_row_in_columns(self):
        columns = []
        if len(self.rows) == 0:
            return []

        columns_length = len(self.rows[0])
        for i in range(columns_length):
            columns.append([row[i] for row in self.rows])
        return columns

    def map_elements_position(self):
        matrix_value_positions = []
        for r_index, row in enumerate(self.rows):
            for c_index, value in enumerate(row):
                matrix_value_positions.append([value, (r_index, c_index)])
        return matrix_value_positions

    def find_max_row_values(self):
        return [index for index, (value, (r, c)) in enumerate(self.positions) if value == max(self.rows[r])]

    def find_min_column_values(self):
        return [index for index, (value, (r, c)) in enumerate(self.positions) if value == min(self.columns[c])]


def saddle_points(matrix):
    if invalid_input_format(matrix):
        raise ValueError('Irregular matrix is not valid.')

    if len(matrix) == 0:
        return [{}]
    matrix = Matrix(matrix)

    max_values_indexes = matrix.find_max_row_values()
    min_values_indexes = matrix.find_min_column_values()
    saddle_indexes = [i for i in max_values_indexes if i in min_values_indexes]

    if len(saddle_indexes) == 0:
        return [{}]
    return [{'row': matrix.positions[i][1][0] + 1, 'column': matrix.positions[i][1][1] + 1} for i in saddle_indexes]


def invalid_input_format(row_lists):
    test_list = set([len(r) for r in row_lists])
    if len(test_list) == 1:
        return False
    return True
