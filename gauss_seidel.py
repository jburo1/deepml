import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
    if x_ini != None : x = x_ini
    else: x = np.zeros(len(b))
    for _ in range(n):
        x_new = np.zeros_like(x, dtype=float)
        for idx in range(len(x)):
            s1 = np.dot(A[idx, :idx], x_new[:idx])
            s2 = np.dot(A[idx, idx+1:], x[idx+1:])
            x_new[idx] = (b[idx] - s1 - s2) / A[idx, idx]
        x = x_new
    return x.round(4).tolist()

A = np.array([[4, 1, 2], [3, 5, 1], [1, 1, 3]], dtype=float)
b = np.array([4, 7, 3], dtype=float)

n = 100
print(gauss_seidel(A, b, n))