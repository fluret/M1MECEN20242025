def separe_nombres(nombres):
    pairs = []
    impairs = []
    for n in nombres:
        if n % 2 == 0:
            pairs.append(n)
        else:
            impairs.append(n)
    return tuple(pairs), tuple(impairs)

print(separe_nombres((1, 2, 3, 4, 5)))
print(separe_nombres((10, 20, 30, 40, 50)))
print(separe_nombres((1, 3, 5, 7, 9)))

val1, val2 = separe_nombres((1, 3, 4, 2, 6, 8, 9, 12))
if val1:
    f"je fais quelque chose avec les pairs"
    
if val2:
    f"je fais quelque chose avec les impairs"
