import numpy as np
def divide_on_feature(X, feature_i, threshold):
    return X[X[:, feature_i] >= threshold], X[X[:, feature_i] < threshold]

print(divide_on_feature(X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]]),
    feature_i = 0,
    threshold = 5))