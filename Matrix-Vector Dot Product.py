def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if(len(a) != len(b) or len(a) == 0 or len(b) == 0):
        return -1
    
    ans = []

    for row in a:
        product = 0
        for i in range(len(b)):
            product += row[i] * b[i]
        ans.append(product)
    
    return ans
