def increment(number):
    return number + 1

increment_v2 = lambda number: number + 1

def high_order_function(number, myFunction):
    return number + myFunction(number)

high_order_function = lambda number, myFunction: number + myFunction(number)

result = high_order_function(100, increment)
print(result)

result = high_order_function(200, increment_v2)
print(result) 