
from sklearn.cluster import KMeans
import numpy as np

# Example mood data: [happiness, sadness, anger]
data = np.array([
    [0.9, 0.1, 0.0],
    [0.1, 0.8, 0.2],
    [0.3, 0.3, 0.4],
    [0.6, 0.2, 0.1]
])

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print("Cluster labels for mood patterns:", kmeans.labels_)
