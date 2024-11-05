# Saisie du nombre de pays
num_countries = int(input("Combien de pays allez-vous saisir ? "))

# Dictionnaire pour stocker les pays et leurs villes
country_city_dict = {}

# Saisie des pays et des villes
for _ in range(num_countries):
    data = input("Saisissez le nom du pays suivi de la liste des villes séparées par un espace : \n").split()
    country = data[0]
    cities = data[1:]
    country_city_dict[country] = cities

# Saisie du nombre de villes à rechercher
num_cities_to_search = int(input("Combien de villes souhaitez-vous rechercher ? "))

# Recherche des villes et affichage des résultats
for _ in range(num_cities_to_search):
    city_to_search = input("Saisissez le nom de la ville à rechercher : ")
    FOUND = False
    for country, cities in country_city_dict.items():
        if city_to_search in cities:
            print(f"{city_to_search} se situe en {country}")
            FOUND = True
            break
    if not FOUND:
        print(f"{city_to_search} n'a pas été trouvé dans les pays saisis.")
