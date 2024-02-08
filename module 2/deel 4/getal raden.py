from time import sleep
import random
rondes_gewonnen = 0
totale_pogingen = 0
print('in dit spel moet je een getal raden tussen 1 en 100')
sleep(1)
print('als je binnen 50 getallen zit ben je warm binnen 20 ben je heel warm')
sleep(1)
print('je krijg ook te zien of je hoger,lager of het hebt geraden')
sleep(1)
begin = input('wil je beginnnen? (ja/nee) ')
if begin == 'ja':
    for i in range(20):
        getal = random.randint(1,100)
        poging = 0
        correct = False
        try:    
            while correct == False or poging > 10:
                antwoord = int(input(f'welk nummer gok je voor cijfer: {i +1}? '))
                sleep(.5)
                if poging >= 10:
                    print('helaas deze ronde heb je verloren')
                if antwoord > getal:
                    print('je bent hoger')
                    poging += 1
                elif antwoord < getal:
                    print('je bent lager')
                    poging += 1
                elif antwoord == getal:
                    correct = True
                    rondes_gewonnen += 1
                    sleep(.5)
                    print('je hebt hem')
                    sleep(.5)
                    totale_pogingen += poging
                if antwoord - getal < 20 and antwoord != getal:
                    print('je bent heel warm')
                elif antwoord - getal < 50 and antwoord != getal:
                    print('je bent warm')
        except ValueError:
            break



print('----game summary----')
print(f'aantal goed: {rondes_gewonnen} van de 20')
print(f'aantal pogingen: {totale_pogingen}')
