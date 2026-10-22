values = [1, 4, 7, 5, 3]
current = 0

while current + 1 < len(values) and values[current + 1] > values[current]:
    current += 1

print("Best value:", values[current])
