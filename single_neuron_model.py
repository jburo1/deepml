import numpy as np


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    features, labels, weights = np.array(
        features), np.array(labels), np.array(weights)
    logits = (features@weights)+bias
    probs = 1.0/(1.0+np.exp(-logits))
    mse = np.sum((labels-probs)**2)/len(features)
    return np.round(probs, 4), float(np.round(mse, 4))


print(single_neuron_model(features=[
      [0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels=[0, 1, 0], weights=[0.7, -0.4], bias=-0.1))
