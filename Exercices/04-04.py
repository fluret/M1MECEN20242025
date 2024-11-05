def trouve_max_min(tup):
    if not tup:
        return None, None
    min_value = min(tup)
    max_value = max(tup)
    return max_value, min_value

print(trouve_max_min((1, 2, 3, 4, 5)))
print(trouve_max_min((10, 20, 30, 40, 50)))
