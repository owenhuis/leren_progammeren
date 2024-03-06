from opdracht01 import *

for _ in range(1):
    watermeloen = {}
    watermeloen['name'] = 'watermelon'
    watermeloen['weight'] = 3000
    watermeloen['color'] = 'green'
    watermeloen['round'] = True
    fruitmand.append(watermeloen)


for naam in fruitmand:
    print(naam['weight'], naam['name'])