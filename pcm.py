import numpy as np

x = list(map(float, input("Enter analog signal values: ").split()))

# Quantization
q = np.round((np.array(x) + 1) * 7 / 2).astype(int)

# PCM
print("PCM:")
for i in q:
    print(format(i, "03b"), end=" ")

# Demodulation
d = q * 2 / 7 - 1

print("\nDemodulated signal:", np.round(d, 2))
