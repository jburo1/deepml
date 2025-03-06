
import numpy as np
import copy
import math

np.random.seed(42)


class Layer(object):
    def set_input_shape(self, shape):
        self.input_shape = shape

        def layer_name(self):
            return self.__class__.__name__

        def parameters(self):
            return 0

        def forward_pass(self, X, training):
            raise NotImplementedError()

        def backward_pass(self, accum_grad):
            raise NotImplementedError()

        def output_shape(self):
            raise NotImplementedError()


class Dense(Layer):
    def __init__(self, n_units, input_shape=None):
        self.layer_input = None
        self.input_shape = input_shape
        self.n_units = n_units
        self.trainable = True
        self.W = None
        self.w0 = None

    def forward_pass():

    def backward_pass(self, accum_grad):

        def number_of_parameters():

            # Initialize a Dense layer with 3 neurons and input shape (2,)
dense_layer = Dense(n_units=3, input_shape=(2,))

# Define a mock optimizer with a simple update rule


class MockOptimizer:
    def update(self, weights, grad):
        return weights - 0.01 * grad


optimizer = MockOptimizer()

# Initialize the Dense layer with the mock optimizer
dense_layer.initialize(optimizer)

# Perform a forward pass with sample input data
X = np.array([[1, 2]])
output = dense_layer.forward_pass(X)
print("Forward pass output:", output)

# Perform a backward pass with sample gradient
accum_grad = np.array([[0.1, 0.2, 0.3]])
back_output = dense_layer.backward_pass(accum_grad)
print("Backward pass output:", back_output)
