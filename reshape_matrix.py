import numpy as np


def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:

    # check if reshape is possible
    if len(a)*len(a[0]) != new_shape[0]*new_shape[1]:
        return []

    reshaped_matrix = []
    flattened = []

    # flatten the input matrix
    for row in a:
        for entry in row:
            flattened.append(entry)

    # slice up flattened array, append to reshaped_matrix
    chunk_size = new_shape[1]
    i, j = 0, chunk_size
    while j <= len(flattened):
        reshaped_matrix.append(flattened[i:j])
        i = i + chunk_size
        j = j + chunk_size

    return reshaped_matrix


print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (4, 2)))

pass
