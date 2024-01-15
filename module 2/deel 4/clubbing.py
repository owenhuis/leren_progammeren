PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

bandje = ('blauw', 'rood')
#bouw hieronder de floowchart na

print('welkom bij coole club')
age = int(input('hoe oud ben je?  '))
if age < 18:
    print('sorry je mag nog niet naar binnen')
    print(f'probeer opnieuw in {18 - age} jaar')
    
else:
    naam = input('wat is je naam?')
    if naam in VIP_LIST:
        if age >= 21:
            band = bandje[0]
        else:
            band = bandje[1]
        print(f'jij krijgt een {band} bandje')
    drinken = input(f'wat wil je drinken?')
    if drinken == 'cola' and bandje == True or drinken == 'bier' and bandje == True:
        print('astublieft complimenten van het huis')