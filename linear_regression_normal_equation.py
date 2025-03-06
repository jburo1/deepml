import numpy as np


def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X, y = np.array(X), np.array(y)
    return np.round(np.linalg.inv(X.T @ X) @ X.T @ y, 4).tolist()


print(linear_regression_normal_equation(
    X=[[1, 1], [1, 2], [1, 3]], y=[1, 2, 3]))

pass
