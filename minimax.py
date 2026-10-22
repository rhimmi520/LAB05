def minimax(depth, node, is_max, values):
    if depth == 2:
        return values[node]

    left = minimax(depth + 1, node * 2, not is_max, values)
    right = minimax(depth + 1, node * 2 + 1, not is_max, values)

    return max(left, right) if is_max else min(left, right)

print("Best value:", minimax(0, 0, True, [3, 5, 2, 9]))
