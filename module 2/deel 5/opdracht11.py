from fruitmand import *

kleuren = []
rond = 0
niet_rond = 0

for kleur in fruitmand:
    if kleur['color'] in kleuren:
        None
    else:
        kleuren.append(kleur['color'])


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