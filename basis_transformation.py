import numpy as np


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    B, C = np.array(B), np.array(C)
    return np.round(np.linalg.inv(C)@B, 4)


print(transform_basis(B=[[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]],
                      C=[[1, 2.3, 3],
                          [4.4, 25, 6],
                         [7.4, 8, 9]]))
