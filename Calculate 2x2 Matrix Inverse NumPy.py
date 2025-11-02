import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:

    matrix = np.array(matrix)
    if np.linalg.det(matrix) == 0:
        return 0

	return np.linalg.inv(matrix)
