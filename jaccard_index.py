import numpy as np


def jaccard_index(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    intersection = np.sum((y_true == 1) & (y_pred == 1))
    union = np.sum((y_true == 1) | (y_pred == 1))
    return round(intersection/union, 3)


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
print(jaccard_index(y_true, y_pred))
