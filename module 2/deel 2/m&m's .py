import random
zak = []
kleuren = ('oranje', 'blauw', 'groen', 'bruin')

hoeveel = int(input("hoeveeel m&m's wil in je zak je? "))
volle_zak = 0
for i in range(hoeveel):
    if volle_zak < hoeveel:
        keuze = random.choice(kleuren)
        zak.append(keuze)

print(zak)
