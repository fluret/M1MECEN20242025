age = int(input("Quel est votre âge ? "))
if 8 <= age < 10:
    print("Le joueur est dans le groupe U8")
elif 10 <= age < 12:
    print("Le joueur est dans le groupe U10")
elif 12 <= age < 14:
    print("Le joueur est dans le groupe U12")
elif 14 <= age < 16:
    print("Le joueur est dans le groupe U14")

if 8 <= age < 10:
    groupe = "U8"
elif 10 <= age < 12:
    groupe = "U10"
elif 12 <= age < 14:
    groupe = "U12"
elif 14 <= age < 16:
    groupe = "U14"
else:
    groupe = "aucun"

print(f"Le joueur est dans le groupe {groupe}")
