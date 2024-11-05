def searchL(element, liste):  
    for index, value in enumerate(liste):
        if value == element:
            return index
    return False

ma_liste = [10, 20, 30, 40, 50]
print(searchL(30, ma_liste))
print(searchL(33, ma_liste))