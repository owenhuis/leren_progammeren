the_list = []
hoeveel = int(input('hoeveel lijstjes wil je?'))

for i in range(1, hoeveel + 1):
    lijst = {}
    aantal_nummers = int(input(f'hoeveel nummers wil je in lijstje {i}?'))
    lijst['nummers'] = list(range(i, aantal_nummers * i + 1, i))
    the_list.append(lijst)

for getallen in the_list:
    print(getallen)