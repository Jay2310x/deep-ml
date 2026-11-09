def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
# for col in range (len(a[0])):
    #     new_row = []
    #     for row in range(len(a)):
    #         new_row.append(a[row][col])

	new = []
	for row in range(len(matrix[0])):
		new_row =[]
		for col in range(len(matrix)):
			new_row.append(scalar * matrix[row][col])

		new.append(new_row)
	return(new)
		