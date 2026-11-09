import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	cov_matrix =np.cov(vectors)
	return cov_matrix.tolist()