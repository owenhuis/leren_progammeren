from time import sleep # zorgt voor een tijdelijke stop
import random # zorgt dat ik een random iets kan gebruiken
rondes_gewonnen = 0 # telt de hoeveelheid rondes
totale_pogingen = 0 # telt de aantal pogingen
poging = False # stopt een crash
stoppen = False # chekt of je wilt stoppen of niet
# print wat er staat \/
print('in dit spel moet je een getal raden tussen 1 en 100')
sleep(1)
print('als je binnen 50 getallen zit ben je warm binnen 20 ben je heel warm')
sleep(1)
print('je krijg ook te zien of je hoger,lager of het hebt geraden')
sleep(1)
# print wat er staat /\
begin = input('wil je beginnnen? (ja/nee) ') # vraagt of je  wilt beginnen
if begin == 'ja': # als je wilt beginnen
    for i in range(20):# gaat het volgende 20x herhalen
        getal = random.randint(1,1000)# maakt een random getal aan
        totale_pogingen += poging # je aantal pogingen worden toegevoegd bij je totale pogingen 
        poging = 0 # zet je poging voor de ronde op 0
        correct = False # zet of je hey antwoord in de ronde goed heb op false
        if stoppen == True:# als je wilt stoppen waar staat dan stop je
            break
        while correct == False or poging >= 10: # herhaalt het volgende tot je meer dan 10 pogingen maakt of wilt stoppen
            try:# probeer het volgende
                antwoord = int(input(f'welk nummer gok je voor cijfer: {i +1}? (poging: {poging}) of zeg q om te stoppen')) # gebruiker vult iets in (een getal) of (q om te stoppen)
                sleep(.5) # wacht even
            except ValueError:#  behalve als er een ValueError is (een letter of een -getal) dan
                stoppen = True # stoppen wordt true
                break # stopt de while
            if poging >= 10: # als je meer dan 10 pogingen doe dan
                print('helaas deze ronde heb je verloren') # print iets uit
                break
            if antwoord > getal: # als je antwoord groter is dan het getal dan
                print('je bent hoger') # print wat er staat
                poging += 1 # poging + 1
            elif antwoord < getal: # als je antwoord kleiner is dan het getal
                print('je bent lager') # print wat er staat
                poging += 1 # poging + 1
            elif antwoord == getal: # als je antwoord gelijk is aan het getal 
                correct = True # je antwoordt wordt gezet op true
                rondes_gewonnen += 1 # aantal rondes gewonnen + 1
                sleep(.5) # wacht 0.5 sec
                print('je hebt hem') # print
                sleep(.5)  # wacht 0.5 sec
            berekenen = antwoord - getal # warm berekennen
            if berekenen < 0: # als warm - getal is
                berekenen = getal - antwoord # andere manier warm berekenen
            if berekenen < 20 and antwoord != getal: # binnen 20
                print('je bent heel warm') # heel warm print
            elif berekenen < 50 and antwoord != getal: # binnen 50
                print('je bent warm') # warm print
# eind print \/
sleep(.5)
print('')
sleep(.5)
print('----game summary----')
print(f'aantal goed: {rondes_gewonnen} van de 20')
print(f'aantal pogingen: {totale_pogingen}')
print(' ')