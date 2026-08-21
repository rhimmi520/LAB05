import math

s = ['A','B','C','D']
f = [5,4,2,1]
total = sum(f)

# Huffman codes
c = ['0','10','110','111']

H = 0
L = 0

print("Symbol\tProbability\tCode")

for i in range(4):
    p = f[i]/total
    H += -p*math.log2(p)
    L += p*len(c[i])
    print(s[i], "\t", round(p,3), "\t\t", c[i])

print("\nEntropy =", round(H,3))
print("Average Length =", round(L,3))
print("Efficiency =", round(H/L*100,2), "%")
