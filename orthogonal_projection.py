import numpy as np
def orthogonal_projection(v, L):
    v,L=np.asarray(v),np.asarray(L)
    return (v@L)/(L@L)*L

v = [3, 4]
L = [1, 0]
print(orthogonal_projection(v, L))