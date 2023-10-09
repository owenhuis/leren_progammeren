#vragenlijst
print('voor de solicitatie moet je een paar vragen be antwoordt')
print()
print()
geslacht = input('ben je man of vrouw? (man/vrouw/anders)  ')
rijbewijs = input('heb je een vrachtwagenrijbewijs? (ja/nee)  ')
hoed = input('bezit je een hoge hoed? (ja/nee)  ')
gewicht = int(input('hoe zwaar ben je in kg?  '))
lengte = int(input('hoe lang ben je in cm?  '))
certificaat_overleven = input('heb je een certificaat voor het overleven met gevaarlijk personeel? (ja/nee)  ')
dieren_of_kleding_ervaring = input('heb je meer dan 4 jaar praktijk evervaring met dieren of dressur? (ja/nee)  ')
jongleer_ervaring = input('heb je 5 of meer jaren ervaring met jongleren? (ja/nee)  ')
acrobatiek_ervaring = input('heb je 3 jaar of langer praktijk ervaring met acrobatiek? (ja/nee)  ')
diploma = input('bezit je een diploma van mbo niveau 4? (ja/nee)  ')
ondernemer = input('ben je ondernemer (ja/nee)  ')
if ondernemer == 'ja':
    ondernemer_tijd = int(input('voor hoelang ben je al een ondernemer?  '))
    if ondernemer_tijd > 3:
        ondernemer_werknemers = int(input('hoeveel werknemers zijn er onder je?  '))
        if ondernemer_werknemers >= 5:
            ondernemer = True
        else:
            ondernemer = False
if geslacht == 'man':
    snor = int(input('hoelang is je snor in cm?  '))
if geslacht == 'vrouw':
    HAAR_LENGTE = 20 #cm
    haar_lengte = input('hoe lang is je haar? (in cm)  ')
    if haar_lengte >= HAAR_LENGTE:
        haarkleur = input('welke kleur haar heb je? (rood,bruin,blond)  ')
        if haarkleur == 'rood':
            krulhaar = input('is je haar krullend? (ja/nee)  ')
if geslacht == 'anders':
    glimlach = int(input('hoe breed = je lach in cm?  '))

#drie keuzes
drie_keuzes = dieren_of_kleding_ervaring == 'ja' or jongleer_ervaring == 'ja' or acrobatiek_ervaring == 'nee'

#diploma of ondernemer
diploma_ondernemer = diploma == 'ja' or ondernemer == True

# min en max gewicht
MIN_GEWICHT = 90 #kg
MAX_GEWICHT = 120 #kg
#min en max lengte
MIN_LENGTE = 150 #cm
MAX_LENGTE = 220 #cm

#snor lengte
SNOR_LENGTE = 10 #cm
#glimlach
GLIMLACH = 10 #cm

#afwijslijst
afwijs_lijst = []

if rijbewijs == 'nee': 
    print('sorry we zoeken alleen een directeur die ook kan rijden')
if hoed == 'nee':
    print('een goede circus directeur heeft een hoge hoed nodig')
if gewicht < MIN_GEWICHT:
    print('sorry maar we zoeken iemand die wat zwaarder is')
if gewicht > MAX_GEWICHT:
    print('sorry maar we zoeken iemand die wat lichter is')
if lengte < MIN_LENGTE:
    print('sorry maar we zoeken iemand wat langer')
if lengte > MAX_LENGTE:
    print('we zoeken iemand die wat kleiner is')
if certificaat_overleven == 'nee':
    print('we zoeken iemand die met gevaarlijk persooneel omkan.')
if drie_keuzes == False:
    print('je moet of dieren, kleding, jongleer of acrobatiek ervaring hebben')
if diploma_ondernemer == False:
    print('je moet of een diploma hebben of een ondernemer zijn')
if geslacht == 'man':
    if snor < SNOR_LENGTE:
        print('we zoeken iemand met een bredere snor')
if geslacht == 'vrouw':
    if haar_lengte < HAAR_LENGTE:
        print('we zoeken iemand met wat langer haar')
    if haarkleur != 'rood':
        print('we zoeken iemand met een andere haarkleur')
        if krulhaar == 'nee':
            print('we zoeken iemand met krulhaar')
if geslacht == 'anders':
    if glimlach < GLIMLACH:
        print('we zoeken iemand met een grotere lach')


#eind resultaat
if not afwijs_lijst:
    print('je bent geschickt om deze circusleider te worden, stuur je cv zo snel mogelijk en wij contact met je op.')

