def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = matrix[row][col] * scalar
            
	return matrix
