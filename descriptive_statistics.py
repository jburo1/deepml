import numpy as np


def descriptive_statistics(data):
    data = np.asarray(data)

    def _calculate_mode(data: np.ndarray):
        uniq = np.unique(data, return_counts=True, equal_nan=False)
        return uniq[0][np.argmax(uniq[1])]
        # vals, counts = np.unique_counts(data)
        # return vals[np.argmax(counts)]

    stats_dict = {
        "mean": np.mean(data),
        "median": np.median(data),
        "mode": _calculate_mode(data),
        "variance": np.round(np.var(data, axis=0, ddof=0), 4),
        "standard_deviation": np.round(np.std(data, axis=0, ddof=0), 4),
        "25th_percentile": np.percentile(data, axis=0, q=25),
        "50th_percentile": np.percentile(data, axis=0, q=50),
        "75th_percentile": np.percentile(data, axis=0, q=75),
        "interquartile_range": np.percentile(data, axis=0, q=75)-np.percentile(data, axis=0, q=25)
    }
    return stats_dict


print(descriptive_statistics([10, 20, 30, 40, 50]))
