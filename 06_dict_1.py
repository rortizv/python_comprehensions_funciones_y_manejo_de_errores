# Modo tradicional de generar un diccionario con los números del 1 al 10
my_dict = {}
for i in range(1, 6):
    my_dict[i] = i * 10

print('Tradicional: ', my_dict)

# Modo dict-comprehensions de generar un diccionario con los números del 1 al 10
my_dict_v2 = {i: i * 10 for i in range(1, 6)}
print('Dict-comprehensions: ', my_dict_v2)


# Generar un diccionario iterando una lista
import random
countries = ["MEX", "COL", "ARG", "USA", "CAN", "BRA", "URU"]
population = {}
for country in countries:
    population[country] = random.randint(1000000, 100000000)

print(population)


population_v2 = {country: random.randint(1000000, 100000000) for country in countries}
print(population_v2)


# Generar un diccionario iterando dos listas
countries = ["MEX", "COL", "ARG", "USA", "CAN", "BRA", "URU"]
cities = ["CDMX", "BOG", "BUE", "NYC", "TOR", "SAO", "MON"]
country_cities = {country: city for (country, city) in zip(countries, cities)}
print(country_cities)