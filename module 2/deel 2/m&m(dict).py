import random
koningsdag = 'oranje'

kleuren = ('rood', 'blauw', 'groen', 'bruin','geel')
zak = {

}

for a in kleuren:
    zak[a] = 0
zak[koningsdag] = 0
print(zak)


hoeveel = int(input("hoeveeel m&m's wil in je zak je? "))

for mms in range(hoeveel):
    keuze = random.choice(kleuren)

    zak[keuze] += 1
    zak[koningsdag] += 1


print(zak)