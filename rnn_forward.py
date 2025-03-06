import numpy as np


def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    input, h, Wx, Wh, b = np.array(input_sequence), np.array(
        initial_hidden_state), np.array(Wx), np.array(Wh), np.array(b)

    for xt in input:
        h = np.tanh(Wx@xt + Wh@h + b)

    return h


input_sequence = [[1.0], [2.0], [3.0]]
initial_hidden_state = [0.0]
Wx = [[0.5]]  # Input to hidden weights
Wh = [[0.8]]  # Hidden to hidden weights
b = [0.0]     # Bias

print(rnn_forward(input_sequence, initial_hidden_state, Wx, Wh, b))
