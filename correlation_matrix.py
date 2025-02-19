import numpy as np

def _calculate_correlation_matrix(A,B):
    meansA=np.mean(A, axis=1)
    meansB=np.mean(B, axis=1)
    corr=np.zeros((v.shape[0],v.shape[0]))
    num_obs=v.shape[1]
    
    
    # this can be vectorized i believe
    for i in range(cov.shape[0]):
        for j in range(cov.shape[1]):
            for k in range(num_obs):
                cov[i][j]+=(v[i][k]-means[i])*(v[j][k]-means[j])
            cov[i][j]/=float(num_obs-1)
    return np.round(cov,3).tolist()
    

def calculate_correlation_matrix(X, Y=None):
    x=np.array(X)
    if Y is not None: y = np.array(Y); return _calculate_correlation_matrix(x,y)
    else: return _calculate_correlation_matrix(x,x)
    
    