# Modo tradicional de generar una lista del 1 al 10
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)


# Modo list-comprehensions de generar una lista del 1 al 10
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

# Imprimir los números pares
numbers = [ 35, 38, 29, 88, 52, 40, 11, 99, 74 ]
even_numbers = [ number for number in numbers if number % 2 == 0 ]
print('Toda la lista de numbers: ', numbers)
print('Números pares: ', even_numbers)


# Modo tradicional de generar una lista del 1 al 10 multiplicando por 2
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)


# Modo list-comprehensions de generar una lista del 1 al 10 multiplicando por 2
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)