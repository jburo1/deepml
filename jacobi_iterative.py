import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    da = np.diag(A)
    nda = A - np.diag(da)
    x = np.zeros(len(b))
    for _ in range(n):
        x = (b - nda @ x) / da
    return x.round(4).tolist()


print(solve_jacobi(
    np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]]), np.array([-1, 2, 3]), 2))
