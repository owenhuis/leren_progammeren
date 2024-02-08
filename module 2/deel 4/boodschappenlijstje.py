#lijst \/
boodschappen_lijst = {}
#je antwoord want anders kan de code kapot gaan
antwoord = False
#functie voor het toevoegen van items \/
def toevoegen (toevoeging, hoeveel_er_in):
    winkelkar = False
    for item in boodschappen_lijst:
        if toevoeging in item:
            #aantal == waarde. de waarde = bijv. ["12x ei"] wordt ["12", "x", "ei"] dan wordt alles er uit gehaald en krijg je alleen "12" en als dan iets wilt toevoegen bijv. 3 ei dan heb je 15
            aantal = int(item.split('x')[0]) + int(hoeveel_er_in)
            boodschappen_lijst[boodschappen_lijst.index(item)] = f'{aantal}x {toevoeging}'
            winkelkar = True
            break
    if winkelkar == False:
        boodschappen_lijst.append(f'{hoeveel_er_in}x {toevoeging}')

# eerste toevoeging \/
toevoeging = input('wat wil je toevoegen? ').lower()
hoeveel_er_in = int(input('hoevaak wil je het toevoegen'))
toevoegen(toevoeging, hoeveel_er_in)
#tweede of meerdere toevoeging \/
while antwoord != 'nee':
    antwoord = input('wil je nog iets toevoegen? (ja/nee)').lower()
    if antwoord == 'ja':
        toevoeging = input('wat wil je toevoegen? ').lower()
        hoeveel_er_in = int(input('hoevaak wil je het toevoegen'))
        toevoegen(toevoeging, hoeveel_er_in)
    elif antwoord == 'nee':
        break
#eind print \/
print(' ')
print(' ')
print('-[ BOODSCHAPPENLIJST ]-')
print(' ')
for item in boodschappen_lijst:
    print(item)
print(' ')
print('-----------------------')