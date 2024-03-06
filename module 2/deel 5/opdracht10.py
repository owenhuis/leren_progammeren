from opdracht01 import *


grootste_fruit = sorted(fruitmand, key= lambda fruit: fruit['weight'], reverse=True)

for gewicht in grootste_fruit:
    print(gewicht['name'],gewicht['weight'] / 1000,'kg')
