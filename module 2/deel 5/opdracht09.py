from fruitmand import *

kleuren = []

for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])
print(kleuren)