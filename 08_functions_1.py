def suma(a, b):
    return int(a) + int(b)

def resta(a, b):
    return int(a) - int(b)

def multiplicacion(a, b):
    return int(a) * int(b)

def division(a, b):
    return int(a) / int(b)

input("Presiona una tecla para iniciar...")
print("Digite dos números para realizar las operaciones")
print("El primer valor: ")
a = input()
print("El segundo valor: ")
b = input()
print("La suma es: ", suma(a, b))
print("La resta es: ", resta(a, b))
print("La multiplicacion es: ", multiplicacion(a, b))
print("La division es: ", division(a, b))
