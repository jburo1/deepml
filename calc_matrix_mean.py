def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means=[]
	
	if mode == 'row':
		for row in matrix:
			acc=0
			for ele in row:
				acc=acc+ele
			means.append(acc/len(matrix[0]))
	else:
		i=0
		while i<len(matrix[0]):
			j=0
			acc=0
			while j<len(matrix):
				acc=acc+matrix[j][i]
				j=j+1
			means.append(acc/len(matrix))
			i=i+1
	
	return means

print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))