# edades = [15, 87, 32, 65, 56, 32, 49, 37]
# # Filtrar las edades mayores a 30
# edades_filtradas = filter(lambda edad: edad > 60, edades)
# print(list(edades_filtradas))

# # Filtrar las edades menores a 30
# edades_filtradas = filter(lambda edad: edad < 30, edades)
# print(list(edades_filtradas))



def filter_by_length(words):
    return filter(lambda word: len(word) > 4, words)

words = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
response = filter_by_length(words)
print(response)