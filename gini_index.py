import numpy as np

def gini_impurity(y):
    y=np.asarray(y)
    p=np.unique(y, return_counts=True, equal_nan=False)[1]/len(y)
    # p=np.unique_counts(y).counts/len(y)
    return np.round(1 - p.T @ p,3)

y = [0, 1, 1, 1, 0]
print(gini_impurity(y))