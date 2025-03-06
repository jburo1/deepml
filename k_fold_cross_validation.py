import numpy as np


def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)
    np.random.shuffle(data)
    split_data = np.array_split(data, k, axis=0)
    listed_data = [d.squeeze().tolist() for d in split_data]
    splits = [[[list(filter(lambda i: i != d, listed_data))], [d]]
              for d in listed_data]
    return splits


print(cross_validation_split(data=np.array(
    [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), k=5))
# print(cross_validation_split(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 2, 42))
