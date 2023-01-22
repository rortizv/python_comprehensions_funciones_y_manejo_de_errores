edades = [15, 87, 32, 65, 56, 32, 49, 37]
edades_v2 = []

# con un ciclo for
for i in edades:
    edades_v2.append(i * 10)

print('List original de edades', edades)
print('Con ciclo for', edades_v2)

# con map
edades_v3 = list(map(lambda x: x * 10, edades))
print('Con map', edades_v3)