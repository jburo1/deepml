import numpy as np


def precision(y_true, y_pred):
    tp, fp = np.sum((y_true == 1) & (y_pred == 1)), np.sum(
        (y_true == 0) & (y_pred == 1))
    return tp / (tp + fp)


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
y_true.any()
result = precision(y_true, y_pred)
print(result)
