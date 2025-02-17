import numpy as np

def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)
    np.random.shuffle(data)    
    data = np.array_split(data,k,axis=0)
    data = [d.tolist() for d in data]
    splits = [[data[np.all(data!=d.tolist())], [d.tolist()]] for d in data]
    return splits
    if len(data) % k == 0: 
        # np.split(data, k, axis=0)  
        splits = [[data[np.all(data!=d,axis=1)].tolist(), [d.tolist()]] for d in data]
    else:
        indices = [k*i+1 for i in range(1,len(data)//k)]
        partition = np.array_split(data, indices, axis=0)
        splits = [[partition[np.all(partition!=d,axis=1)].tolist(), d.tolist()] for d in partition]
    return splits
    
print(cross_validation_split(data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), k = 5))
# print(cross_validation_split(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 2, 42))

