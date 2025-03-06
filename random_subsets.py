import numpy as np


def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
    np.random.seed(seed)

    subsets = []
    n_samples = X.shape[0]

    for _ in range(n_subsets):
        if replacements:
            indices = np.random.choice(
                n_samples, size=n_samples, replace=replacements)
        else:
            indices = np.random.choice(
                n_samples, size=n_samples//n_subsets+1, replace=replacements)
        # else: indices = np.random.choice(n_samples, size=n_samples, replace=replacements)

        X_subset = X[indices]
        y_subset = y[indices]

        subsets.append((X_subset, y_subset))

    return subsets


print(get_random_subsets(X=np.array([[1, 2],
                                     [3, 4],
                                     [5, 6],
                                     [7, 8],
                                     [9, 10]]),
                         y=np.array([1, 2, 3, 4, 5]),
                         n_subsets=3,
                         replacements=False))
