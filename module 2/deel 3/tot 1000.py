hoeveelheid = 50
toevoegen = 51
while hoeveelheid < 1000:
    hoeveelheid = hoeveelheid + toevoegen
    print(hoeveelheid)
    toevoegen += 1
    if hoeveelheid >= 1000:
        break
print('nu heb je meer dan of duizend getallen')