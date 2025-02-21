import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
    mat = np.asarray(dense_matrix).T
    values = mat[mat!=0]
    col_idx = np.nonzero(mat)[1]
    row_ptr = np.zeros(mat.shape[0] + 1,dtype=int)
    row_ptr[1:] = np.cumsum(np.count_nonzero(mat, axis=1))
    return values.tolist(), col_idx.tolist(), row_ptr.tolist()

dense_matrix = [
    [0, 0, 3, 0],
    [1, 0, 0, 4],
    [0, 2, 0, 0]
]

vals, row_idx, col_ptr = compressed_col_sparse_matrix(dense_matrix)
print(vals, row_idx, col_ptr)