from opdracht01 import *
import random
namen_lijst = []

hoeveel = int(input('hoeveel wil je items? '))
for naam in fruitmand:
    namen_lijst.append(naam['name'])

for i in range(hoeveel):
    fruit = random.choice(namen_lijst)
    print(fruit)