n = int(input('Entrez la taille du damier : '))

for i in range(n):
    ligne = ''
    for j in range(n):
        if (i + j) % 2 == 0:
            ligne += 'X'
        else:
            ligne += 'O'
    print(ligne)
