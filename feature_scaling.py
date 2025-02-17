import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data=(data-data.mean(axis=0))/data.std(axis=0)
    dmin,dmax=np.min(data,axis=0),np.max(data,axis=0)
    normalized_data = (data - dmin)/(dmax-dmin)
    dmin,dmax=np.min(normalized_data,axis=0),np.max(normalized_data,axis=0)
    normalized_data*=(dmax-dmin)
    normalized_data+=dmin 
    return standardized_data, normalized_data

print(feature_scaling(data = np.array([[1, 2], [3, 4], [5, 6]])))

pass