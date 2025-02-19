import numpy as np

def to_categorical(x:np.ndarray, n_col=None):
    if not n_col: n_col = x.max()+1
    # select rows of I(nxn) according to x
    return np.eye(x.size,n_col)[x] 
    
print(to_categorical(x = np.array([0, 1, 2, 1, 0])))