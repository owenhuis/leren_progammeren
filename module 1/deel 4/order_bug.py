getal_1 = int(input('hoeveel is getal 1?  '))
getal_2 = int(input('hoeveel is getal 2?  '))
resultaat = getal_1 / getal_2
if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    print ("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))

def vraag_getal(aantal):
    antwoord = input("Voer het "+ antwoord +" getal in: ")
    getal = int(aantal)
    return getal

def deel_getallen(a, b):
    return a / b