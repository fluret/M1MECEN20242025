ma_liste = ['T', 'O', 'A', 'p', 't', 
            'p', 'l', 'o', 'e', 's', 't','t', 'r', 
            's', 't', 't', 't','u', 'm',
            'm', 'p']

nouvelle_liste = []
for index, val in enumerate(ma_liste):
    if index % 2 != 0:
        nouvelle_liste.append(val)

ma_liste = nouvelle_liste

print(ma_liste)

nouvelle_liste = []
for val in ma_liste:
    if val != 't':
        nouvelle_liste.append(val)

ma_liste = nouvelle_liste
print(ma_liste)
