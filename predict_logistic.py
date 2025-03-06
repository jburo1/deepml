import numpy as np


def sigmoid(z: float) -> float:
    return np.round(1.0 / (1.0 + np.exp(-z)), 4)


def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    preds = sigmoid(X@weights + bias)
    return np.where(preds >= 0.5, 1, 0)


print(predict_logistic(
    np.array([[1, 1], [2, 2], [-1, -1], [-2, -2]]), np.array([1, 1]), 0))
print(predict_logistic(
    np.array([[0, 0], [0.1, 0.1], [-0.1, -0.1]]), np.array([1, 1]), 0))
