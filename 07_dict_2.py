import random
countries = ["MEX", "COL", "ARG", "USA", "CAN", "BRA", "URU"]
population_v2 = {country: random.randint(1000000, 100000000) for country in countries}
print(population_v2)

result = {country: population for (country, population) in
population_v2.items() if population > 50000000 }
print(result)

text = 'Come to the dark side'
unique = { char: char.upper() for char in text if char in 'aeiou'}
print(unique)