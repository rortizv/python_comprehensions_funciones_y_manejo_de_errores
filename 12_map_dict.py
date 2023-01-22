items = [
    {
        'product_name': 'laptop',
        'price': 1000
    },
    {
        'product_name': 'mouse',
        'price': 50
    },
    {
        'product_name': 'keyboard',
        'price': 100
    }
]

# Cómo obtener sólo una lista con los precios?
prices = list(map(lambda x: x['price'], items))
print(prices)

# Cómo obtener sólo una lista con los nombres de los productos?
names = list(map(lambda x: x['product_name'], items))
print(names)

# Modificar cada objeto agregándole la propiedad 'taxes' con el valor 0.19
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

def calculate_total(item):
    new_item = item.copy()
    new_item['total'] = new_item['price'] + item['taxes']
    return new_item


new_items = list(map(add_taxes, items))
print('With taxes, before total: ', new_items)

new_items = list(map(calculate_total, new_items))
print('With taxes, after total: ', new_items)

print('Items originales: ', items)
