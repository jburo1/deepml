import numpy as np
from itertools import combinations_with_replacement    
def create_exponent_configurations(feature_combinations:list[tuple], num_features):
    exponent_list = [[feature_combo.count(i) for i in range(num_features)] for feature_combo in feature_combinations]
    return np.array(exponent_list)

def polynomial_features(X, degree):
    X = np.asarray(X)
    num_features=X.shape[1]
    feature_combinations = [combo for i in range(degree+1) for combo in combinations_with_replacement(range(num_features),i)]
    exponent_configurations=create_exponent_configurations(feature_combinations, num_features)
    # for each row in X, calculate corresponding monomials up to degree 
    monomials = np.power(X[:, :, None], np.arange(degree + 1))
    # use exponent_configurations to generate the polynomials
    poly_features = np.prod(monomials[:, np.arange(num_features), exponent_configurations], axis=2)
    return poly_features
    
X = np.array([[2, 3],[3, 4],[5, 6]])
degree = 2
output = polynomial_features(X, degree)
print(output)