def searchL2(elements, liste):  
    resultat = []
    trouve = False
    for element in elements:
        for index, value in enumerate(liste):
            if value == element:
                resultat.append(index) 
                trouve = True
        if not trouve:
            resultat.append(False)
        trouve = False
    return resultat


ma_liste = [150, 20, 30, 70, 200, "Coucou", 'toto']
a_chercher = [250, 30, "Coucou", "vélo"]

print(searchL2(a_chercher, ma_liste))
