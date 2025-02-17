import numpy as np
def find_closest_centroid(point,centroids):
    distances = np.linalg.norm(centroids-point,axis=1)
    return centroids[np.argmin(distances)]

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    points, centroids = np.array(points), np.array(initial_centroids)
    for _ in range(max_iterations):
        centroid_point_labels = np.array([find_closest_centroid(point, centroids) for point in points])
        new_centroids = []
        for i in range(k):
            mask = np.all(centroid_point_labels == centroids[i], axis=1)
            mean_value = np.mean(points[mask], axis=0)
            new_centroids.append(mean_value)
        new_centroids = np.array(new_centroids)
        centroids = new_centroids
    return centroids    

print(k_means_clustering(points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], k = 2, initial_centroids = [(1, 1), (10, 1)], max_iterations = 10))

pass