def get_population():
    keys = [ 'col', 'bra', 'arg', 'usa', 'mex' ]
    values = [ 4000, 10000, 3000, 15000, 800 ]
    return keys, values

def get_population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
