import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    v=np.array(vectors)
    means=np.mean(v, axis=1, keepdims=True)
    num_obs=v.shape[1]
    cov = (v-means)@((v-means).T)/(num_obs-1)
    return np.round(cov,3).tolist()

print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]))