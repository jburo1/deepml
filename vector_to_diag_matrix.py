import numpy as np


def make_diagonal(x: np.ndarray):
    return np.diag(x)


print(make_diagonal(x=np.array([1, 2, 3])))
