# see ridge regressino: a historical context
import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    mse = np.sum((y_true - X@w)**2)/X.shape[0]
    regularization = alpha * np.sum(w**2)
    return mse + regularization


X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

loss = ridge_loss(X, w, y_true, alpha)
print(loss)