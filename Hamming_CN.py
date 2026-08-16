# Hamming Code - Error Detection and Correction

data = input("Enter 4-bit data: ")

# Data bits
d1, d2, d3, d4 = map(int, data)

# Calculate parity bits
p1 = d1 ^ d2 ^ d4
p2 = d1 ^ d3 ^ d4
p4 = d2 ^ d3 ^ d4

# Hamming code: p1 p2 d1 p4 d2 d3 d4
code = [p1, p2, d1, p4, d2, d3, d4]

print("Hamming Code:", ''.join(map(str, code)))

# Receive code
received = list(map(int, input("Enter received 7-bit code: ")))

# Calculate error position
s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
s4 = received[3] ^ received[4] ^ received[5] ^ received[6]

error = s4 * 4 + s2 * 2 + s1

if error == 0:
    print("No error detected.")
else:
    print("Error at position:", error)
    received[error - 1] ^= 1
    print("Corrected Code:", ''.join(map(str, received)))
