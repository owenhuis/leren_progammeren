pizzas = [
    {"naam": "Margherita","diameter": 30, "ingrediënten": ["tomatensaus", "mozzarella", "basilicum"]},
    {"naam": "Pepperoni", "diameter": 40, "ingrediënten": ["tomatensaus", "mozzarella", "pepperoni"]},
    {"naam": "Hawaï", "diameter": 35, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "ananas"]},
    {"naam": "Quattro Stagioni", "diameter": 38, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "champignons", "artisjokken", "olijven"]},
    {"naam": "Funghi", "diameter": 33, "ingrediënten": ["tomatensaus", "mozzarella", "champignons", "oregano"]},
    {"naam": "Napolitana", "diameter": 32, "ingrediënten": ["tomatensaus", "mozzarella", "ansjovis", "kappertjes", "olijven"]},
    {"naam": "Capricciosa", "diameter": 36, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "champignons", "artisjokken"]},
    {"naam": "Quattro Formaggi","diameter": 37,"ingrediënten": ["tomatensaus", "mozzarella", "gorgonzola", "parmezaanse kaas", "fontina"]},
    {"naam": "Vegetarisch","diameter": 39,"ingrediënten": ["tomatensaus", "mozzarella", "paprika", "ui", "olijven", "champignons"]},
    {"naam": "Tonno","diameter": 34,"ingrediënten": ["tomatensaus", "mozzarella", "tonijn", "ui", "olijven"]}
]
# naam
for pizza in pizzas:
    print(pizza['naam'])
# diameter + naam
for pizza in pizzas:
    print({pizza["naam"]}, {pizza['diameter']})

# de grootste
def get_diameter(a):
    return a['diameter']
grootste_pizza = max(pizzas, key=get_diameter)
grootste_pizza2 = max(pizzas, key= lambda pizza: pizza['diameter'])
print(grootste_pizza)
print(grootste_pizza2)

#van klein naar groot\/
kleinste_pizza = sorted(pizzas, key= lambda pizza: pizza['diameter'])
print(kleinste_pizza)