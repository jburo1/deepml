import numpy as np


def recall(y_true, y_pred):
    tp, fn = np.sum((y_true == 1) & (y_pred == 1)), np.sum(
        (y_true == 1) & (y_pred == 0))
    return np.round(tp / (tp + fn), 4)


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

print(recall(y_true, y_pred))
