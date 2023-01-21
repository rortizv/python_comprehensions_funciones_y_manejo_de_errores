set_countries = { 'col', 'bra', 'arg' }
size = len(set_countries)
print(size)

# Para saber si un elemento está dentro de un set/array/lista/diccionario/lo que sea
print('col' in set_countries)
print('pe' in set_countries)


# add
set_countries.add('uru')
print(set_countries)

# update
set_countries.update({'par', 'bol'})
print(set_countries)

# delete
set_countries.remove('bra')
print(set_countries)

# eliminar todo
set_countries.clear()
print(len(set_countries))