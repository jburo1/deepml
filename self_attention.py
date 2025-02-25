import numpy as np

def softmax(X):
    arr = np.array(X)
    exp_arr = np.exp(arr - np.max(arr, axis=-1, keepdims=True))
    return np.round(exp_arr / np.sum(exp_arr, axis=-1, keepdims=True), 4)

def compute_qkv (X, W_q, W_k, W_v):
    return X@W_q, X@W_k, X@W_v

def self_attention(Q, K, V):
    return softmax((Q @ K.T) / np.sqrt(K.shape[-1]))@V

X = np.array([[1, 0], [0, 1]])
W_q = np.array([[1, 0], [0, 1]])
W_k = np.array([[1, 0], [0, 1]])
W_v = np.array([[1, 2], [3, 4]])

Q, K, V = compute_qkv(X, W_q, W_k, W_v)
output = self_attention(Q, K, V)

print(output)