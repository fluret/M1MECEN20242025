def trouve(tup, element):
    for index, valeur in enumerate(tup):
        if valeur == element:
            return index
    return -1

exemple_tuple = (1, 2, 3, 4, 5)

position = trouve(exemple_tuple, 3)

print(f'La valeur 3 se trouve à la position {position} dans le tuple {exemple_tuple}')

