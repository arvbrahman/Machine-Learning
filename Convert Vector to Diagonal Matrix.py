import numpy as np

def make_diagonal(x):
	
    Dm = [[0]*x for _ in x]

    for i in range(len(Dm)):
        for j in range(len(Dm[0])):
            if(i == j):
                Dm[i][j] = x[i]

    return Dm
