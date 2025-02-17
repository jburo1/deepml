import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    v=np.array(vectors)
    means=np.mean(v, axis=1)
    cov=np.zeros((v.shape[0],v.shape[0]))
    num_obs=v.shape[1]
    
    for i in range(cov.shape[0]):
        for j in range(cov.shape[1]):
            for k in range(num_obs):
                cov[i][j]+=(v[i][k]-means[i])*(v[j][k]-means[j])
            cov[i][j]/=float(num_obs-1)
    return np.round(cov,3).tolist()

print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]))

pass