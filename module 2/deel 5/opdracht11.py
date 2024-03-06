from opdracht01 import *

kleuren = []
rond = 0
niet_rond = 0

for color in fruitmand:
    kleuren.append(color['color'])

kleur = input(f'welke kleur wil je kiezen? {kleuren} ')

for fruit in fruitmand:
    if fruit['color'] == kleur:
        if fruit['round']:
            rond += 1
        else:
            niet_rond += 1

if rond > niet_rond:
    print(f'er is {rond - niet_rond} meer ronde dan niet ronde')
elif rond < niet_rond:
    print(f'er is {niet_rond - rond} meer niet ronde dan wel ronde')
else:
    print('er zijn evenveel ronde als niet ronde')