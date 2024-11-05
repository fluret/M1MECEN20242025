num_countries = int(input("Combien de pays souhaitez vous saisir ?"))

country_city_dict = {}

for _ in range(num_countries):
    data = input("Saisir le nom du pays et la liste des villes séparées par un espace : ").split()
    country = data[0]
    cities = data[1:]
    country_city_dict[country] = cities
num_villes_a_chercher = int(input("Combien de villes souhaitez vous chercher ?"))

for _ in range(num_villes_a_chercher):
    ville = input("Saisir le nom de la ville à chercher : ")
    for country, cities in country_city_dict.items():
        if ville in cities:
            print(f"{ville} est dans le pays {country}")
            break
    else:
        print(f"{ville} n'est pas dans la liste des villes saisies")
