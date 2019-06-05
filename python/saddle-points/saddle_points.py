def saddle_points(matrix):
    if len(matrix) == 0:
        return [{}]

    if irregular_dimensions(matrix):
        raise ValueError('Irregular matrix dimensions')

    columns = build_matrix_columns(matrix)

    saddle_values = []
    for ind_r, i in enumerate(matrix):
        for ind_c, j in enumerate(i):
            if max(i) == min(columns[ind_c]):
                saddle_values.append({'row': ind_r + 1, 'column': ind_c + 1})

    if len(saddle_values) == 0:
        return [{}]
    return saddle_values


def irregular_dimensions(matrix):
    distinct_row_dimensions = set([len(m) for m in matrix])
    return len(distinct_row_dimensions) > 1


def build_matrix_columns(matrix_rows):
    columns = []
    for i in range(len(matrix_rows[0])):
        c = [m[i] for m in matrix_rows]
        columns.append(c)
    return columns
