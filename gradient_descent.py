import numpy as np


def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
    X, y, weights = np.asarray(X), np.asarray(y), np.asarray(weights)
    for i in range(n_iterations):
        match method:
            case "batch":
                weights -= (2 * learning_rate) * ((X@weights - y)@X)/len(X)
            case "stochastic":
                for n in range(len(X)):
                    weights -= (2 * learning_rate) * \
                        ((X[n]@weights) - y[n]) * X[n]
            case "mini_batch":
                indices = np.arange(len(X))
                indices_split = np.array_split(indices, batch_size)
                X_splits = X[indices_split]
                y_splits = y[indices_split]
                for x_split, y_split in zip(X_splits, y_splits):
                    weights -= (2 * learning_rate) * \
                        ((x_split@weights - y_split)@x_split)/len(x_split)
    return weights


# Sample data
X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
y = np.array([2, 3, 4, 5])

# Parameters
learning_rate = 0.01
n_iterations = 1000
batch_size = 2

# Initialize weights
weights = np.zeros(X.shape[1])

# Test Batch Gradient Descent
final_weights = gradient_descent(
    X, y, weights, learning_rate, n_iterations, method='batch')
print(final_weights)
# Test Stochastic Gradient Descent
final_weights = gradient_descent(
    X, y, weights, learning_rate, n_iterations, method='stochastic')
print(final_weights)
# Test Mini-Batch Gradient Descent
final_weights = gradient_descent(
    X, y, weights, learning_rate, n_iterations, batch_size, method='mini_batch')
print(final_weights)
