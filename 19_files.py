file = open('./text.txt')
# Leer todo el archivo
# print(file.read())

# Leer una linea a la vez
print(file.readline())
print(file.readline())


for line in file:
    print(line)

file.close()

# Leer todas las lineas y cerrar el archivo una vez termine - método que más se usa
with open('./text.txt') as file:
    for line in file:
        print(line)
