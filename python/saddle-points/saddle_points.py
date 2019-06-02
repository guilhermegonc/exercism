def saddle_points(matrix):
    if len(matrix) == 0:
        return [{}]
    if len(matrix) > 0:
        test = len(matrix[0])
        for r in matrix:
            if len(r) != test:
                raise ValueError('Irregular matrix is not valid.')

    columns = []
    for i in range(len(matrix[0])):
        columns.append([row[i] for row in matrix])

    candidates = {}
    for row_index, r in enumerate(matrix):
        for column_index, c in enumerate(r):
            if c == max(r):
                candidates[(row_index, column_index)] = c

    answer = []
    for c in candidates.items():
        if c[1] <= min(columns[c[0][1]]):
            bola = {'row': c[0][0] + 1, 'column': c[0][1] + 1}
            answer.append(bola.copy())
    if len(answer) == 0:
        return [{}]
    return answer


matrix = [[]]
print(saddle_points(matrix))
