import random
koningsdag = 'oranje'

kleuren = ('rood', 'blauw', 'groen', 'bruin','geel')
zak = {

}

hoeveel = int(input("hoeveeel m&m's wil in je zak je? "))

for mms in range(hoeveel):
    keuze = random.choice(kleuren)
    if not keuze in zak:
        zak[keuze] = 0
    zak[keuze] += 1
    if not koningsdag in zak:
        zak[koningsdag] = 0
    zak[koningsdag] += 1


print(zak)