import numpy as np
def softmax(X):
    arr = np.array(X)
    exp_arr = np.exp(arr - np.max(arr, axis=-1, keepdims=True))
    return np.round(exp_arr / np.sum(exp_arr, axis=-1, keepdims=True), 4)
print(softmax(scores = [1, 2, 3]))