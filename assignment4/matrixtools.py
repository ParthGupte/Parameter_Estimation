import numpy as np

def F(m:np.ndarray,x:float):
    return m[0]*np.exp(m[1]*x) + m[2]*np.exp(m[3]*(x**2))

def norm(m:np.ndarray):
    return sum(m**2)



    
