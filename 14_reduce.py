# Calcular la suma de todos los números de una list

import functools

numbers = [1, 2, 3, 4]

def accumulator(counter, item):
    print('Counter: ', counter)
    print('Item: ', item)
    return counter + item

result = functools.reduce(accumulator, numbers)
print(result)