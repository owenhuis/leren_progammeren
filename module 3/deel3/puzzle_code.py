# see speek sequence

import time
nummer = [1]
nieuw_getal = []
getalhoeveelheid = []
drieopeenrij = False
round_one = True
while drieopeenrij == False:
    nieuw_getal = []
    laatste_getal = None


    for getal in nummer:
        if round_one == False and (getal == 1 or (laatste_getal is None or laatste_getal == 1)):
            getalhoeveelheid.append(1)
            laatste_getal = 1
        elif getal == 2 or (laatste_getal is None or laatste_getal == 2):
            getalhoeveelheid.append(2)
            laatste_getal = 2
        elif getal == 3 or (laatste_getal is None or laatste_getal == 3):
            getalhoeveelheid.append(3)
            laatste_getal = 3
            if len(getalhoeveelheid) == 3:
                drieopeenrij = True
                break
        else:
            if laatste_getal == 1:
                nieuw_getal.append(1 + len(getalhoeveelheid) * 10)
            elif laatste_getal == 2:
                nieuw_getal.append(2 + len(getalhoeveelheid) * 10)
            elif laatste_getal == 3:
                nieuw_getal.append(3 + len(getalhoeveelheid)* 10)
            getalhoeveelheid.clear()
            getalhoeveelheid.append(getal)
            laatste_getal = getal

        if round_one == True:
            nieuw_getal.append(11)
            round_one = False
        else:
            if laatste_getal == 1:
                nieuw_getal.append(1 + len(getalhoeveelheid) * 10)
            elif laatste_getal == 2:
                nieuw_getal.append(2 + len(getalhoeveelheid) * 10)
            elif laatste_getal == 3:
                nieuw_getal.append(3 + len(getalhoeveelheid) * 10)
    nummer = nieuw_getal
    print(nummer)
    time.sleep(.5)
    


print('final number:', nummer)
