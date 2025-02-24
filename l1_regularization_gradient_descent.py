import numpy as np

def l1_regularization_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float = 0.1, 
                                       learning_rate: float = 0.01, max_iter: int = 1000, 
                                       tol: float = 1e-4) -> tuple:
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0
    for _ in range(max_iter):
        y_hat = X@weights + bias
        residuals = y_hat - y
        loss = (1.0/2.0) * np.mean((residuals)**2) + alpha * np.sum(abs(weights))
        grad_w = (X.T@residuals)/n_samples + alpha * np.sign(weights)
        grad_b = np.mean(residuals,axis=0)
        weights -= learning_rate * grad_w
        bias -= learning_rate * grad_b
        if np.linalg.norm(grad_w, ord=1) < tol: break
    return weights, bias


X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

alpha = 0.1
weights, bias = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000)
print(weights, bias)