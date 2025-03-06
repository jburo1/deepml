import numpy as np


def sigmoid(z: float) -> float:
    return np.round(1.0 / (1.0 + np.exp(-z)), 4)


print(sigmoid(0))
