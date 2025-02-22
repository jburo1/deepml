import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    poly_features=[[d**i for i in range(degree+1)] for d in data]
    return poly_features

print(phi_transform(data = [1.0, 2.0], degree = 2))