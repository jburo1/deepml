import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    input, h0, Wx = np.array(input_sequence), np.array(initial_hidden_state), np.array(WX),
    h1 = np.tanh(Wh@initial_hidden_state + Wx@input_sequence + b)
    return final_hidden_state