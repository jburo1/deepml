import numpy as np
import math


def batch_iterator(X, y=None, batch_size=64):
    xacc = np.array_split(X, math.ceil(len(X)/batch_size))
    if y is not None:
        yacc = np.array_split(y, math.ceil(len(y)/batch_size))
        return list(zip(xacc, yacc))
    return xacc


X = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8],
              [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))
