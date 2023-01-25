age = 10
if age < 18:
    print("Your age is under 18")
    raise Exception("You are not old enough to vote.")
    
print("Esta linea no se va a ejecutar")