import numpy as np

def cosine_similarity(v1:np.ndarray, v2:np.ndarray):
    assert v1.shape == v2.shape
    assert v1.size > 0 and v2.size > 0
    eps = 1e-8
    dp = np.dot(v1, v2)
    v1_l2, v2_l2 = np.dot(v1, v1), np.dot(v2, v2)
    return np.round(dp/(np.sqrt(v1_l2) * np.sqrt(v2_l2) + eps),3)

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))