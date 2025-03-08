import math


def normal_pdf(x, mean, std_dev):
    val = (1.0 / (std_dev * math.sqrt(2.0 * math.pi))) * \
        math.exp((-1.0 / 2.0) * ((x - mean) ** 2) / (std_dev ** 2))
    return round(val, 5)


print(normal_pdf(x=16, mean=15, std_dev=2.04))
