import numpy as np
def log_softmax(scores: list) -> np.ndarray:
    x = np.asarray(scores)
    return x - np.max(x) - np.log(np.sum(np.exp(x-max(x))))

def unstable_log_softmax(x):
    return np.log(np.exp(x)/np.sum(np.exp(x)))

def stable_log_softmax(x):
    return x - np.max(x) - np.log(np.sum(np.exp(x-max(x))))

def log_softmax(scores: list) -> np.ndarray:
    return np.round(unstable_log_softmax(scores),4), np.round(stable_log_softmax(scores),4)
    return np.round(stable_log_softmax(scores),4)

A = np.array([50, 50, 50])
print(log_softmax(A))
unstable, stable = log_softmax(A)
print(np.isclose(unstable, stable))