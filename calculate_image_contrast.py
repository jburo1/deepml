import numpy as np

def calculate_contrast(img) -> int:
    return np.max(img)-np.min(img)

print(calculate_contrast(img = np.array([[0, 50], [200, 255]])))