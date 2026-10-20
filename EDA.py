import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    'A': [10, 20, 20, 30, 40],
    'B': [15, 25, 35, 45, 55]
})

print("Mean:\n", data.mean())
print("Median:\n", data.median())
print("Mode:\n", data.mode().iloc[0])

plt.boxplot(data['A'])
plt.show()

plt.scatter(data['A'], data['B'])
plt.show()

data['A'].value_counts().plot(kind='bar')
plt.show()

plt.hexbin(data['A'], data['B'], gridsize=10)
plt.show()
