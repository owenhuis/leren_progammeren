#vragenlijst
print('voor de solicitatie moet je een paar vragen be antwoordt')
print()
print()
rijbewijs = input('heb je een vrachtwagenrijbewijs? (ja/nee)  ')
hoed = input('bezit je een hoge hoed? (ja/nee)  ')
gewicht = int(input('hoe zwaar ben je in kg?  '))
lengte = int(input('hoe lang ben je in cm?  '))
certificaat_overleven = input('heb je een certificaat voor het overleven met gevaarlijk personeel? (ja/nee)  ')
dieren_of_kleding_ervaring = input('heb je meer dan 4 jaar praktijk evervaring met dieren of dressur? (ja/nee)  ')
jongleer_ervaring = input('heb je 5 of meer jaren ervaring met jongleren? (ja/nee)  ')
acrobatiek_ervaring = input('heb je 3 jaar of langer praktijk ervaring met acrobatiek? (ja/nee)  ')
diploma = ('bezit je een diploma van mbo niveau 4? (ja/nee)  ')
ondernemer = ('ben je ondernemer (ja/nee)')
if ondernemer == 'ja':
    ondernemer_tijd = int(input('voor hoelang ben je al een ondernemer?  '))
    if ondernemer_tijd == 3:
        ondernemer_werknemers = int(input('hoeveel werknemers zijn er onder je?  '))
        if ondernemer_werknemers >= 5:
            ondernemer == True
        else:
            ondernemer == False

# min en max gewicht
MIN_GEWICHT = 90
MAX_GEWICHT = 120
#min en max lengte
MIN_LENGTE = 150
MAX_LENGTE = 220
#eind resultaat
if (gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT) and (lengte >= MIN_LENGTE and lengte <= MAX_LENGTE) and rijbewijs == 'ja' and hoed == 'ja' and certificaat_overleven == 'ja' and (dieren_of_kleding_ervaring == 'ja' or jongleer_ervaring == 'ja' or acrobatiek_ervaring == 'ja'):
    print('je bent geschickt om deze circusleider te worden stuur je cv zo snel mogelijk en dan zien we je over 2 weken om 15:00')
else:
    print('helaas je bent niet wat we zoeken')