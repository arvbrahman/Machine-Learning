def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    a,b = matrix[0]
    c,d = matrix[1]

    m = (a+d)/2
    p = (a*d) - (b*c)

    eigens = []
    A = m + ((m*m) - p)**0.5
    B = m - ((m*m) - p)**0.5

    eigens.append(A)
    eigens.append(B)

    return eigens
    

