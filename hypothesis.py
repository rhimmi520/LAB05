from scipy.stats import ttest_1samp

data = [12, 14, 15, 13, 16, 14, 15]

t, p = ttest_1samp(data, 14)

print("Test Statistic:", t)
print("P-value:", p)

if p < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")
