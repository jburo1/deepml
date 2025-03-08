import math


def binomial_probability(n, k, p):
    probability = math.comb(n, k) * p ** k * (1-p) ** (n-k)
    return round(probability, 5)


print(binomial_probability(n=6, k=2, p=0.5))
