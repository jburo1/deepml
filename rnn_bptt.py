import numpy as np
import copy


class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.hidden_size = hidden_size
        self.W_xh = np.random.randn(hidden_size, input_size)*0.01
        self.W_hh = np.random.randn(hidden_size, hidden_size)*0.01
        self.W_hy = np.random.randn(output_size, hidden_size)*0.01
        self.b_h = np.zeros((hidden_size, 1))
        self.b_y = np.zeros((output_size, 1))
        self.hts = []
        self.yts = []

    def forward(self, x):
        self.hts.clear()
        self.yts.clear()
        ht = np.zeros((self.hidden_size,))
        for xt in x:
            ht = np.tanh(self.W_xh@xt + self.W_hh@ht + self.b_h)
            yt = self.W_hy@ht + self.b_y
            self.hts.append(ht.copy())
            self.yts.append(yt.copy())
        return self.yts

    def backward(self, x, y, learning_rate):

        pass


input_sequence = np.array([[1.0], [2.0], [3.0], [4.0]])
expected_output = np.array([[2.0], [3.0], [4.0], [5.0]])
# Initialize RNN
rnn = SimpleRNN(input_size=1, hidden_size=5, output_size=1)

# Forward pass
output = rnn.forward(input_sequence)

# Backward pass
rnn.backward(input_sequence, expected_output, learning_rate=0.01)

print(output)

# The output should show the RNN predictions for each step of the input sequence.
