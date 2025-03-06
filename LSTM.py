import numpy as np


class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    @staticmethod
    def _sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    def forward(self, x, initial_hidden_state, initial_cell_state):
        hts = []
        ht = initial_hidden_state.copy()
        ct = initial_cell_state.copy()
        for xt in x:
            xt = xt.reshape(self.input_size, 1)
            concat_ht_xt = np.concatenate((ht, xt))
            ft = self._sigmoid(self.Wf @ concat_ht_xt + self.bf)
            it = self._sigmoid(self.Wi @ concat_ht_xt + self.bi)
            ct_tilde = np.tanh(self.Wc @ concat_ht_xt + self.bc)
            ct = ft * ct + it * ct_tilde
            ot = self._sigmoid(self.Wo @ concat_ht_xt + self.bo)
            ht = ot * np.tanh(ct)

            hts.append(ht.copy())

        return hts, hts[-1], ct


input_sequence = np.array([[1.0], [2.0], [3.0]])
initial_hidden_state = np.zeros((1, 1))
initial_cell_state = np.zeros((1, 1))

lstm = LSTM(input_size=1, hidden_size=1)
outputs, final_h, final_c = lstm.forward(
    input_sequence, initial_hidden_state, initial_cell_state)

print(final_h)
