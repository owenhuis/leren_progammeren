boodschappen_lijst = []
antwoord = False

def toevoegen (toevoeging, hoeveel_er_in):
    if toevoeging in boodschappen_lijst:
        hoeveel_er_in += hoeveel_er_in
    return boodschappen_lijst.append(f'{hoeveel_er_in}x {toevoeging}')

toevoeging = input('wat wil je toevoegen? ')
hoeveel_er_in = input('hoevaak wil je het toevoegen')
toevoegen(toevoeging, hoeveel_er_in)

while antwoord != 'nee':
    antwoord = input('wil je nog iets toevoegen? (ja/nee)')
    if antwoord == 'ja':
        toevoeging = input('wat wil je toevoegen? ')
        hoeveel_er_in = input('hoevaak wil je het toevoegen')
        toevoegen(toevoeging, hoeveel_er_in)
    elif antwoord == 'nee':
        break

print(boodschappen_lijst)