from fruitmand import *

def get_weight (fruit):
    return fruit['weight']


grootste_fruit = sorted(fruitmand, key= get_weight, reverse=True)

for gewicht in grootste_fruit:
    print(gewicht['name'],gewicht['weight'] / 1000,'kg')
