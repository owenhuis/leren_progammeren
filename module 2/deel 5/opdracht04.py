from fruitmand import *
import random
namen_lijst = []

hoeveel = int(input('hoeveel wil je items? '))
for fruit in fruitmand:
    namen_lijst.append(fruit['name'])

for i in range(hoeveel):
    fruit = random.choice(namen_lijst)
    print(fruit)