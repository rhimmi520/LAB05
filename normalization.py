from sklearn.preprocessing import MinMaxScaler, StandardScaler

x = [[20], [40], [60], [80], [100]]

print("Normalization:")
print(MinMaxScaler().fit_transform(x))

print("Standardization:")
print(StandardScaler().fit_transform(x))
