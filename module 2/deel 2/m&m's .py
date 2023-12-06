import random
zak = []
kleuren = ('oranje', 'blauw', 'groen', 'bruin')

hoeveel = int(input("hoeveeel m&m's wil in je zak je? "))
volle_zak = 0
for i in range(hoeveel):
    if volle_zak < hoeveel:
        keuze = random.choice(kleuren)
        zak.append(keuze)

aantal_van_oranje = zak.count('oranje')
aantal_van_blauw = zak.count('blauw')
aantal_van_groen = zak.count('groen')
aantal_van_bruin = zak.count('bruin')
print(zak)
print('aantal bruine: ',aantal_van_bruin)
print('aantal blauwe: ', aantal_van_blauw)
print('aantal groene: ', aantal_van_groen)
print('aantal oranje: ', aantal_van_oranje)