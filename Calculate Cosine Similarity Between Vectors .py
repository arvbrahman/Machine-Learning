
import numpy as np

def cosine_similarity(v1, v2):
	
    if(len(v1) != len(v2) or len(v1) == 0 or len(v2) == 0):
        return 0

    dot_product = np.dot(v1,v2)

    v1_mag = np.sqrt(np.sum(v1*v1))
    v2_mag = np.sqrt(np.sum(v2*v2))

    return round(dot_product/(v1_mag*v2_mag),3)
