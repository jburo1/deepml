import numpy as np


def rmse(y_true, y_pred):

    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    n = y_true.shape[0]
    rmse = np.sqrt(np.mean((y_true-y_pred)**2))
    return round(rmse, 3)


y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])
print(rmse(y_true, y_pred))
