from math import sqrt
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	assert len(matrix) == len(matrix[0]) == 2
	eigenvalues = []
	a,b,c,d=matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1]
	tra,det=-(a+d),a*d-b*c	
	root1=(-tra+sqrt(tra**2-4*det))/2
	root2=(-tra-sqrt(tra**2-4*det))/2
	eigenvalues.append(root1)
	eigenvalues.append(root2)
	return sorted(eigenvalues, reverse=True)

print(calculate_eigenvalues([[2, 1], [1, 2]]))