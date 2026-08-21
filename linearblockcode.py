import numpy as np

D = list(map(int, input("Enter 4-bit data: ")))

G = np.array([
    [1,0,0,1,1,0,0],
    [0,1,0,1,0,1,0],
    [0,0,1,0,1,1,0],
    [0,0,0,1,1,1,1]
])

C = np.dot(D, G) % 2
print("Codeword:", C)

R = list(map(int, input("Enter received 7-bit code: ")))

if list(C) == R:
    print("No error")
else:
    print("Error detected")
