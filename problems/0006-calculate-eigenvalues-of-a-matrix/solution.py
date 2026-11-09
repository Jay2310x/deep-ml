import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	trace = a+d
	det = (a*d) - (b*c)
	l1, l2= (trace + math.sqrt(trace**2-4*det))/2, (trace - math.sqrt(trace**2-4*det))/2
	eigenvalues = sorted([l1,l2], reverse = True)
	return eigenvalues