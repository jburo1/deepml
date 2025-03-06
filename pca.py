import numpy as np


def pca(data: np.ndarray, k: int) -> np.ndarray:
    standardized_data = (data-data.mean(axis=0))/data.std(axis=0)
    covariance_matrix = np.cov(standardized_data.T)
    evals, evecs = np.linalg.eig(covariance_matrix)
    # form feature vector of top-k principal components
    sorted_evalvecs = sorted(
        zip(evals, evecs.T), key=lambda x: np.abs(x[0]), reverse=True)
    pcs = np.array([vec for _, vec in sorted_evalvecs[:k]])
    return np.round(pcs, 4)


print(pca(data=np.array([[1, 2], [3, 4], [5, 6]]), k=1))
# print(pca(np.array([[4,2,1],[5,6,7],[9,12,1],[4,6,7]]),2))
