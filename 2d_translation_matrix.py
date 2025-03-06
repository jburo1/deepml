import numpy as np


def translate_object(points, tx, ty):
    homogeneous_points = np.array([[x, y, 1] for x, y in points]).T

    T = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    translated_points = T @ homogeneous_points

    return list(zip(translated_points[0], translated_points[1]))


points = [[0, 0], [1, 0], [0.5, 1]]
tx, ty = 2, 3
print(translate_object(points, tx, ty))
