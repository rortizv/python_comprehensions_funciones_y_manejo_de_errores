try:
    print(0/0)
except ZeroDivisionError as error:
    print("Error: ", error)

try:
    assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as error:
    print("Error: ", error)


try:
    age = 10
    if age < 18:
        print("Your age is under 18")
        raise Exception("You are not old enough to vote.")
except Exception as error:
    print("Error: ", error)