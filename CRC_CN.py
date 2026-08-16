data = input("Enter data bits: ")
divisor = input("Enter divisor: ")

# Add zeros
code = data + "0" * (len(divisor) - 1)
code = list(code)

# Modulo-2 division
for i in range(len(data)):
    if code[i] == "1":
        for j in range(len(divisor)):
            code[i + j] = str(int(code[i + j]) ^ int(divisor[j]))

remainder = "".join(code[-(len(divisor) - 1):])

print("CRC Remainder:", remainder)
print("Transmitted Code:", data + remainder)
