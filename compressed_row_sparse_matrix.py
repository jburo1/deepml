import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    mat = np.asarray(dense_matrix)
    values = mat[mat!=0]
    col_idx = np.nonzero(mat)[1]
    row_ptr = np.zeros(mat.shape[0] + 1,dtype=int)
    row_ptr[1:] = np.cumsum(np.count_nonzero(mat, axis=1))
    return values.tolist(), col_idx.tolist(), row_ptr.tolist()

dense_matrix = [
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [3, 0, 4, 0],
    [1, 0, 0, 5]
]

vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
print("Values array:", vals)
print("Column indices array:", col_idx)
print("Row pointer array:", row_ptr)