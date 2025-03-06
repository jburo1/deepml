import math


def elu(x: float, alpha: float = 1.0) -> float:
    val = 0.0
    if x > 0:
        val = x
    else:
        val = alpha * (math.exp(x) - 1.0)
    return float(round(val, 4))


print(elu(-1))
