import numpy as np
from copy import deepcopy

def round(x):
    return np.round(x,4)

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):  	
    features,weights,bias=np.array(deepcopy(features)),np.array(deepcopy(initial_weights)),deepcopy(initial_bias)
    mse_values = []
    n = len(features)
    for _ in range(epochs):
        # forward pass
        logits=(features@weights)+bias
        probs=sigmoid(logits)
        mse_values.append(np.sum((probs-labels)**2)/n)   
        # backward pass
        # calculate derivative of loss wrt to weights and bias
        weight_derivatives = (2.0/n)*(features.T@((probs-labels)*probs*(1-probs)))
        bias_derivative=(2.0/n)*np.sum((probs-labels)*probs*(1-probs))
        # update weights, bias
        weights=weights-learning_rate*weight_derivatives
        bias=bias-learning_rate*bias_derivative
        
    return round(weights).tolist(), float(round(bias)), round(mse_values).tolist()

print(train_neuron(features = [[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]], labels = [1, 0, 0], initial_weights = [0.1, -0.2], initial_bias = 0.0, learning_rate = 0.1, epochs = 1000))

