
nummer = [1]

drieopeenrij = False
round_one = True
print(nummer)
while drieopeenrij == False:
    print(nummer)
    nieuw_getal = []
    getalhoeveelheid = []
    laatste_getal = None

    for getal in nummer:
        if getal == 1 and (laatste_getal is None or laatste_getal == 1) and round_one == False:
            getalhoeveelheid.append(1)
            laatste_getal = 1
        elif getal == 2 and (laatste_getal is None or laatste_getal == 2):
            getalhoeveelheid.append(2)
            laatste_getal = 2
        elif getal == 3 and (laatste_getal is None or laatste_getal == 3):
            getalhoeveelheid.append(3)
            laatste_getal = 3
            if len(getalhoeveelheid) == 3:
                drieopeenrij = True
                break
        else:
            if laatste_getal == 1:
                nieuw_getal.append(10 + len(getalhoeveelheid))
            elif laatste_getal == 2:
                nieuw_getal.append(20 + len(getalhoeveelheid))
            elif laatste_getal == 3:
                nieuw_getal.append(30 + len(getalhoeveelheid))
            getalhoeveelheid.clear()
            getalhoeveelheid.append(getal)
            laatste_getal = getal

    if round_one:
        nieuw_getal.append(11)
        round_one = False
    else:
        if laatste_getal == 1:
            nieuw_getal.append(10 + len(getalhoeveelheid))
        elif laatste_getal == 2:
            nieuw_getal.append(20 + len(getalhoeveelheid))
        elif laatste_getal == 3:
            nieuw_getal.append(30 + len(getalhoeveelheid))

    nummer = nieuw_getal


print('final number:', nummer)
