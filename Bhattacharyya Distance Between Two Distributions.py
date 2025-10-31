import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    if(len(p) != len(q) or len(p) == 0 or len(q) == 0):
        return 0.0
    p = np.array(p)
    q = np.array(q)
    bc = np.sum(np.sqrt(p*q))
    return round(-np.log(bc),4)
