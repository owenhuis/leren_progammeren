from time import sleep
vertaal_woorden = {
    'hoi': 'doei',
    'doei': 'hoi',
    'blub': 'blaf',
    'piraat': 'olifant',
    'vogel': 'mens',
}

zin = 'de piraat zij hoi tegen zijn vogel terwijl de vis blub en doei zij daar schrok de olifant van'
gespleete_zin = zin.split()
vertaalde_zin = ' '.join(vertaal_woorden.get(woord, woord)for woord in gespleete_zin)

print('de eerste zin:')
sleep(1)
print(zin)
sleep(1)
print('')
sleep(2)
print('vertaalde zin')
sleep(1)
print(vertaalde_zin)