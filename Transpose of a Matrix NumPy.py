import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    trans = np.array(a)
    b = trans.transpose()
	return b
