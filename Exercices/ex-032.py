# Lecture du nombre de lignes
n = int(input())

# Initialisation d'un dictionnaire pour stocker les fréquences des mots
frequences = {}

# Lecture des lignes de texte
for _ in range(n):
    ligne = input().strip().lower().split()  # On normalise à minuscule et on sépare par mots
    for mot in ligne:
        if mot in frequences:
            frequences[mot] += 1  # Si le mot existe déjà, on incrémente
        else:
            frequences[mot] = 1  # Si le mot n'existe pas, on l'initialise à 1

# Créer une liste de tuples (fréquence, mot)
liste_frequences = []
for mot, freq in frequences.items():
    liste_frequences.append((freq, mot))

# Trier d'abord par fréquence décroissante puis par ordre lexicographique en cas d'égalité
liste_frequences.sort()

# Afficher les mots, un par ligne
for freq, mot in liste_frequences:
    print(f'{mot:<15} ---> {freq:>10}')
