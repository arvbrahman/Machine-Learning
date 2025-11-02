def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:

    a,b = matrix[0]
    c,d = matrix[1]

    p = (a*d) - (b*c)
    if p == 0:
        return 0
    
    matrix = [[d, -b] , [-c, a]]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (1/p)*matrix[i][j]

	return matrix
