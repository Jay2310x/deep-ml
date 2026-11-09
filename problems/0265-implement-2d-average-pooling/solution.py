def avg_pool_2d(input_matrix: list[list[float]], pool_size: int) -> list[list[float]]:
	"""
	Perform 2D average pooling on the input matrix.
	
	Args:
		input_matrix: 2D input array of shape (H, W)
		pool_size: Size of the square pooling window
		
	Returns:
		2D array after average pooling of shape (H//pool_size, W//pool_size)
	"""
	# Your code here
	rows = len(input_matrix)
	cols = len(input_matrix[0])

	output = []

	for i in range (0, rows, pool_size):
		row=[]
		for j in range (0, cols, pool_size):
			block_sum=0

			for x in range(pool_size):
				for y in range (pool_size):
					block_sum += input_matrix[i + x][j + y]

			avg = block_sum / (pool_size * pool_size)
			row.append(avg)
		output.append(row)
	return output

