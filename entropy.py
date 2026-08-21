import math

p = list(map(float, input("Enter the probabilities: ").split()))

entropy = 0

for x in p:
    if x > 0:
        info = -math.log2(x)
        print("Information Bits:", round(info, 3))
        entropy += x * info

print("Entropy:", round(entropy, 3))
