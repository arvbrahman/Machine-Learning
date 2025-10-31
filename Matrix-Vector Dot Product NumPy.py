import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

	if(len(a) != len(b) or len(a) == 0 or len(b) == 0):
        return -1
    
    mat = np.array(a)
    lis = np.array(b)
    ans = np.matmul(mat,lis)

    return ans.tolist()
