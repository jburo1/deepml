import numpy as np
def softmax(scores: list[float]) -> list[float]:
    arr = np.array(scores)
    return np.round(np.exp(arr)/sum(np.exp(arr)),4)
print(softmax(scores = [1, 2, 3]))