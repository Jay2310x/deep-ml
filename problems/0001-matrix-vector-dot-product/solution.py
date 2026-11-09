def matrix_dot_vector(a: list[list[int | float]], 
                      b: list[int | float]) -> list[int | float] | int:
    # Check if matrix is empty
    if not a or not a[0]:
        return -1

    # Check dimension compatibility
    if len(a[0]) != len(b):
        return -1

    result = []

    # Loop over each row
    for row in a:
        total = 0

        # Compute dot product
        for j in range(len(b)):
            total += row[j] * b[j]

        result.append(total)

    return result