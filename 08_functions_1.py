def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

input("Presiona una tecla para iniciar...")
print("Digite dos números para realizar las operaciones")
print("El primer valor: ")
a = int(input())
print("El segundo valor: ")
b = int(input())
print("La suma es: ", suma(a, b))
print("La resta es: ", resta(a, b))
print("La multiplicacion es: ", multiplicacion(a, b))
print("La division es: ", division(a, b))
