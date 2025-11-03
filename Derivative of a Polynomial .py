#import numpy as np

def poly_term_derivative(c: float, x: float, n: float) -> float:
    
    a = n*c
    b = x**(n-1)
    result = a*b 
    #result = n * c * np.power(x,n-1)
    return result
