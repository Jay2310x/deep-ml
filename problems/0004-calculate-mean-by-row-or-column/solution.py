def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if mode == 'row':
        for row in matrix:
            row_means = sum(row) / num_cols
            means.append(row_means)

    if mode == 'column':
        for c in range(num_cols):
            col_sum = 0
            for r in range(num_rows):
                col_sum += matrix[r][c]
            means.append(col_sum / num_rows)

    return means