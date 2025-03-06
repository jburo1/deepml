import numpy as np


def calculate_dot_product(vec1, vec2) -> float:
    assert vec1.shape == vec2.shape
    return np.dot(vec1, vec2)


print(calculate_dot_product(vec1=np.array(
    [1, 2, 3]), vec2=np.array([4, 5, 6])))
