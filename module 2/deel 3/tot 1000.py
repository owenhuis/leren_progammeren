START_GETAL = 50
hoeveelheid = 50
toevoegen = 51

print(hoeveelheid)
while hoeveelheid < 1000:
    print(f'{START_GETAL} + [] = {hoeveelheid}')
    hoeveelheid = hoeveelheid + toevoegen
    toevoegen += 1
    if hoeveelheid >= 1000:
        print('nu heb je meer dan of duizend getallen')
        break

