def increment(number):
    return number + 1

increment_v2 = lambda number: number + 1

result = increment(100)
print(result)

result = increment_v2(200)
print(result)

full_name = lambda first_name, last_name: f'Full name {first_name.title()} {last_name.title()}'
text = full_name('Raph','Ortiz')
print(text)