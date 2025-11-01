import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    matrix = np.array(matrix)

    means = []
    if(mode == "row"):
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                sum += matrix[i][j]
            mean = sum/len(matrix[0])
            means.append(mean)

    if(mode == "column"):
        matrix = matrix.T
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                sum += matrix[i][j]
            mean = sum/len(matrix[0])
            means.append(mean)

    return means
