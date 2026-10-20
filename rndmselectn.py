import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare, weibull_min

# Random Selection
print("Random Selection:", np.random.choice([1, 2, 3, 4, 5]))

# Binomial Distribution
print("Binomial:", np.random.binomial(10, 0.5, 5))

# Chi-Square Test
print("Chi-Square:", chisquare([20, 30, 50]))

# Weibull Distribution
x = weibull_min.rvs(2, size=100)
plt.hist(x, bins=10)
plt.title("Weibull Distribution")
plt.show()
