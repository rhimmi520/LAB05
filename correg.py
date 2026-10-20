import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

# Correlation
print("Correlation:", np.corrcoef(x, y)[0, 1])

# Linear Regression
slope, intercept, r, p, err = linregress(x, y)
print("Slope:", slope)
print("Intercept:", intercept)

plt.scatter(x, y)
plt.plot(x, np.array(x)*slope + intercept)
plt.show()
