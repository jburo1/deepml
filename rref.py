import numpy as np


def rref(matrix):
    if len(matrix) == 0:
        raise ValueError
    mat = np.asarray(matrix, dtype=float)
    next_pivot_row = 0
    rows = len(mat)
    cols = len(mat[0])

    for col in range(cols):
        for row in range(next_pivot_row, rows):
            if mat[row, col] != 0:
                # swap if not at correct row
                mat[[row, next_pivot_row], :] = mat[[next_pivot_row, row], :]

                # scale entire row
                mat[next_pivot_row, :] /= mat[next_pivot_row, col]

                # adjust all other rows
                for i in range(rows):
                    if i != next_pivot_row:
                        mat[i, :] -= (mat[next_pivot_row, :] * mat[i, col])

                next_pivot_row += 1
                # break
    return np.round(mat, 4)


matrix = []

# matrix = [[0,1],[1,0]]

# matrix = [[0, 2, 1],
#           [1, 0, 1],
#           [0, 1, 1]]

matrix = np.array([
    [1, 2, -1, -4],
    [2, 3, -1, -11],
    [-2, 0, -3, 22]
])

rref_matrix = rref(matrix)
print(rref_matrix)
