import numpy as np

def cosine_similarity(vec1, vec2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	result = 0
	s1 = 0
	s2 = 0
	for i in range(len(vec1)):
		result += vec1[i] * vec2[i]
		s1 += vec1[i]**2
		s2 += vec2[i]**2
	s1 = s1**0.5
	s2 = s2**0.5
	return result /(s1 * s2)