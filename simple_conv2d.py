import numpy as np
def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    kernel_height, kernel_width = kernel.shape
    padded_matrix = np.pad(input_matrix, padding)
    vertical_positions = ((padded_matrix.shape[0] - kernel_height) // stride) + 1
    horizontal_positions = ((padded_matrix.shape[1] - kernel_width) // stride) + 1
    output_matrix = np.zeros((vertical_positions, horizontal_positions))
    
    for i in range(output_matrix.shape[0]):
        iid = i * stride
        for j in range(output_matrix.shape[1]):
            jid = j * stride
            image_window = padded_matrix[iid:iid+kernel_height,jid:jid+kernel_width]
            output_matrix[i][j] = np.sum(image_window * kernel)
    return output_matrix


input_matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

kernel = np.array([
    [1, 0],
    [-1, 1]
])

padding = 1
stride = 2

output = simple_conv2d(input_matrix, kernel, padding, stride)
print(output)

##
input_matrix = np.array([ [1., 2., 3., 4., 5.], 
                         [6., 7., 8., 9., 10.],
                         [11., 12., 13., 14., 15.], 
                         [16., 17., 18., 19., 20.], 
                         [21., 22., 23., 24., 25.], ]) 
kernel = np.array([ [.5, 3.2], [1., -1.], ]) 
padding, stride = 2, 2 
expected = np.array([ [ -1., 1., 3., 5., 7., 15.], [ -4., 16., 21., 26., 31., 35.], [ 1., 41., 46., 51., 56., 55.], [ 6., 66., 71., 76., 81., 75.], [ 11., 91., 96., 101., 106., 95.], [ 42., 65., 68., 71., 74., 25.], ]) 
output = simple_conv2d(input_matrix, kernel, padding, stride) 
print(output)


##
input_matrix = np.array([ [1., 2., 3., 4., 5.], 
                         [6., 7., 8., 9., 10.], 
                         [11., 12., 13., 14., 15.], 
                         [16., 17., 18., 19., 20.], 
                         [21., 22., 23., 24., 25.], ]) 
kernel = np.array([ [1., 2.], 
                   [3., -1.], ]) 
padding, stride = 0, 1 
expected = np.array([ [ 16., 21., 26., 31.], [ 41., 46., 51., 56.], [ 66., 71., 76., 81.], [ 91., 96., 101., 106.], ]) 
output = simple_conv2d(input_matrix, kernel, padding, stride) 
print(output)