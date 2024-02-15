winkelkar = {}

def item():
    product = input('Welk product wil je?  ')
    hoeveel = int(input('Hoe vaak wil je het?  '))
    if product in winkelkar:
        winkelkar[product] += hoeveel
    else:
        winkelkar[product] = hoeveel
# eerste toevoegen
item()
antwoord = input('Wil je nog iets toevoegen? (ja/nee)').lower()
#tweede of meerdere toevoegen
while antwoord != 'nee': 
    if antwoord == 'ja':
        item() 
        antwoord = input('Wil je nog iets toevoegen? (ja/nee)').lower()
    elif antwoord == 'nee':
        break

#eind print
print(' ')
print(' ')
print('-[ BOODSCHAPPENLIJST ]-')
print(' ')
for product, hoeveelheid in winkelkar.items():
    print(f'{hoeveelheid}x {product}')
print(' ')
print('-----------------------')
