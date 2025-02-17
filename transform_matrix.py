import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    a,t,s=np.array(A,dtype=float),np.array(T,dtype=float),np.array(S,dtype=float)
    if t.shape[0]!=t.shape[1]:return -1
    if np.linalg.matrix_rank(t) < t.shape[0]:return -1
    if np.linalg.matrix_rank(s) < s.shape[0]:return -1
    if t.shape[1]!=a.shape[0] or a.shape[1]!=s.shape[0]:return -1
    t_ = np.linalg.inv(t)
    result=t_@a@s 
    return np.round(result,3).tolist()

print(transform_matrix([[1, 2], [3, 4]],[[2, 0], [0, 2]],[[1, 1], [0, 1]]))
print(transform_matrix([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 0], [0, 2]]))