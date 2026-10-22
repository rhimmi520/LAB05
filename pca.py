from sklearn.decomposition import PCA

X = [[2, 3], [3, 4], [4, 5], [5, 6]]

pca = PCA(n_components=1)
result = pca.fit_transform(X)

print(result)
