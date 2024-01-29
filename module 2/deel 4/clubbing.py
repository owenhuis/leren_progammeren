PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

bandje = ('blauw', 'rood')
stempel = False
band = False
sap = False

def leeftijd(age):
    if age < 18:
        return print(f'probeer opnieuw in: {18 - age} jaar')


def drink_prijs(drank, sap):
    if drank == 'cola':
        return print(f'hier is je cola dat is dan €{PRIJS_COLA}0')
    if band or stempel == True:
        if drank == 'bier':
            return print(f'hier is je bier dat is dan €{PRIJS_BIER}0')
        elif drank == 'champagne' and band == 'rood':
            return print(f'hier is je champagne dat is dan €{PRIJS_CHAMPAGNE}0')
    else:
        sap = False
        return print(f'je mag geen alchol onder de 21 probeer opnieuw in: {21 - age} jaar')
#bouw hieronder de floowchart na

print('welkom bij coole club')
age = int(input('hoe oud ben je?  '))
#vierkant 1
if age < 18:
    print('sorry je mag nog niet naar binnen')
    leeftijd(age)
else:
    naam = input('wat is je naam? ')
    if naam in VIP_LIST:
        if age >= 21:
            bandje = bandje[0]
            band = True
        else:
            bandje = bandje[1]
            band = True
        print(f'jij krijgt een {bandje} bandje')
    else:
        if age >= 21:
            print('jij krijgt een stempel van mij')
            stempel = True
        else:
            None
    drinken = input(f'wat wil je drinken?  ')

    #vierkant 2
    while sap == False:
        if drinken == 'champagne' and bandje == False:
            print('alleen vips mogen drinken')
        if drinken == 'cola' and band == True or drinken == 'bier' and band == True:
            print('alsjeblieft van het huis')
            sap = True
        elif drinken != 'cola' and drinken != 'bier' and drinken != 'champagne':
            print('ik weet niet wat je bedoelt hier heb je water')
            sap = True
        else:
            sap = True
            drink_prijs(drinken, sap) 