import mod

# keys, values = mod.get_population()
# print(keys, values)

data = [
    { 'Country': 'col', 'Population': 4000 },
    { 'Country': 'bra', 'Population': 10000 },
    { 'Country': 'arg', 'Population': 3000 },
    { 'Country': 'usa', 'Population': 15000 },
    { 'Country': 'mex', 'Population': 800 }
]

result = mod.get_population_by_country(data, 'bra')
print(result)