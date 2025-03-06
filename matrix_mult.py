import numpy as np


def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:
    A, B = np.array(a, dtype=float), np.array(b, dtype=float)
    if A.shape[1] != B.shape[0]:
        return -1
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            for k in range(A.shape[1]):
                C[i][j] += A[i][k]*B[k][j]
    return np.round(C, 3).tolist()


print(matrixmul([[1, 2], [2, 4]], [[2, 1], [3, 4]]))

pass
