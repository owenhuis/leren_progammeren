PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')


stempel = False
band = False
sap = False

def leeftijd(age):
    if age < 18:
        return print(f'probeer opnieuw in: {18 - age} jaar')


def drink_prijs(drank, band, stempel, bandje):
    if drank == 'cola':
        return f'hier is je cola dat is dan €{PRIJS_COLA}0'
    if drank == 'bier' and stempel:
        return f'hier is je bier dat is dan €{PRIJS_BIER}0'
    elif drank == 'champagne' and bandje == 'blauw':
        return f'hier is je champagne dat is dan €{PRIJS_CHAMPAGNE}0'
    elif drank == 'champagne' and bandje == 'rood':
        return 'alleen vips krijgen champange '
    return 'blub'
    
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
            bandje = 'blauw'
            band = True
        else:
            bandje = 'rood'
            band = True
        print(f'jij krijgt een {bandje} bandje')
    else:
        if age >= 21:
            print('jij krijgt een stempel van mij')
            stempel = True
        else:
            None
    

    #vierkant 2
    while sap != True:
        drinken = input(f'wat wil je drinken?  ')
        if sap == True:
            break
        if drinken == 'champagne' and band == False:
            print('alleen vips mogen drinken')
        elif drinken == 'cola' and band == True or drinken == 'bier' and band == True:
            print('alsjeblieft van het huis')
            sap = True
        elif drinken != 'cola' and drinken != 'bier' and drinken != 'champagne':
            print('ik weet niet wat je bedoelt hier heb je water')
            sap = True
        elif age < 21 and bandje == False and age < 21 and stempel == False:
            print(f'je mag geen alchol onder de 21 probeer opnieuw in: {21 - age} jaar')
        if sap == False:
            prijs = drink_prijs(drinken, band, stempel, bandje)
            print(prijs)
            sap = True 