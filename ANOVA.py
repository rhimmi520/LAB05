from scipy.stats import f_oneway, kruskal

A = [10, 12, 14, 16]
B = [20, 22, 24, 26]
C = [15, 17, 19, 21]

# ANOVA Test
f, p = f_oneway(A, B, C)
print("ANOVA:", f, p)

# Kruskal-Wallis Test
h, p = kruskal(A, B, C)
print("Kruskal-Wallis:", h, p)
