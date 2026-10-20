import numpy as np

data = [10, 20, 30, 40, 50]
means = []

for i in range(1000):
    sample = np.random.choice(data, size=len(data), replace=True)
    means.append(np.mean(sample))

print("Mean:", np.mean(data))
print("Uncertainty (Std):", np.std(means))
print("95% CI:", np.percentile(means, [2.5, 97.5]))
