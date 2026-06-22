from sklearn.cluster import KMeans

X = [[1, 2], [2, 3], [8, 8], [9, 9]]
model = KMeans(n_clusters=2)
model.fit(X)
print(model.labels_)