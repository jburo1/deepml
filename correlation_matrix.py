import numpy as np


def _calculate_correlation_matrix(A, B):
    N = A.shape[0]
    std_A, std_B = np.std(A, axis=0, ddof=1), np.std(B, axis=0, ddof=1)
    means_A, means_B = np.mean(A, axis=0), np.mean(B, axis=0)
    corr_matrix = 1.0/(N-1) * 1.0/np.outer(std_A, std_B) * \
        ((A-means_A).T@(B-means_B))
    return corr_matrix


def calculate_correlation_matrix(X, Y=None):
    x = np.array(X)
    if Y is not None:
        y = np.array(Y)
        return _calculate_correlation_matrix(x, y)
    else:
        return _calculate_correlation_matrix(x, x)


X = np.array([[1, 2],
              [3, 4],
              [5, 6]])
output = calculate_correlation_matrix(X)
print(output)
