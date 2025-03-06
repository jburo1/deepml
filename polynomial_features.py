import numpy as np
from itertools import combinations_with_replacement


def create_poly_features_for_row(row, exponent_configurations, max_degree):
    # for each feature, evaluate all monomials of up to degree max(exponents)
    # can use a dict for this, key = feature idx, value = list of monomials,
    # where value at each index corresponds to monomial of degree index
    feature_monomials = {}
    for idx, feature in enumerate(row):
        monomials = [feature ** i for i in range(max_degree+1)]
        feature_monomials[idx] = monomials

    # using the exponents list, evaluate the polynomials
    poly_features_row = []
    for exponent_configuration in exponent_configurations:
        acc = 1
        for idx, exponent_value in enumerate(exponent_configuration):
            acc *= feature_monomials[idx][exponent_value]
        poly_features_row.append(int(acc))
    # return row as list
    return poly_features_row


def create_exponent_configurations(feature_combinations: list[tuple], num_features):
    exponent_list = []
    for feature_combination in feature_combinations:
        t = *(feature_combination.count(i) for i in range(num_features)),
        exponent_list.append(t)
    return exponent_list


def polynomial_features(X, degree):
    num_features = X.shape[1]
    fidx = [i for i in range(num_features)]
    feature_combinations = []
    for i in range(degree+1):
        feature_combinations.extend(combinations_with_replacement(fidx, i))
    exponent_configurations = create_exponent_configurations(
        feature_combinations, num_features)
    return [create_poly_features_for_row(row, exponent_configurations, degree) for row in X]


X = np.array([[2, 3], [3, 4], [5, 6]])
degree = 2
output = polynomial_features(X, degree)
print(output)
