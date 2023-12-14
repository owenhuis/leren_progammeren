from time import sleep
vertaal_woorden = {
    'hoi': 'doei',
    'doei': 'hoi',
    'blub': 'blaf',
    'piraat': 'olifant',
    'vogel': 'mens',
}

zin = 'de piraat zei hoi tegen zijn vogel terwijl de vis blub en doei zei daar schrok de olifant van'
gespleete_zin = zin.split()
print(gespleete_zin)

getelde_zin = len(gespleete_zin)
for index in range(getelde_zin):
    print(gespleete_zin[index])
    if gespleete_zin[index] in vertaal_woorden:
        gespleete_zin[index] = vertaal_woorden[gespleete_zin[index]]

vertaalde_zin = ' '.join(gespleete_zin)

print('de eerste zin:')
sleep(1)
print(zin)
sleep(1)
print('')
sleep(2)
print('vertaalde zin')
sleep(1)
print(vertaalde_zin)