winkelkar = {}

antwoord = 'ja'
#tweede of meerdere producten toevoegen
while antwoord != 'nee':
    product = input('Welk product wil je?  ')
    hoeveel = int(input('Hoe vaak wil je het?  '))
    if product in winkelkar:
        winkelkar[product] += hoeveel
    else:
        winkelkar[product] = hoeveel
    antwoord = input('Wil je nog iets toevoegen? (ja/nee)').lower()
    # elif antwoord == 'nee':
    #     break

print(winkelkar)
#eind print
print(' ')
print(' ')
print('-[ BOODSCHAPPENLIJST ]-')
print(' ')
for product, hoeveelheid in winkelkar.items():
    print(f'{hoeveelheid}x {product}')
print(' ')
print('-----------------------')
