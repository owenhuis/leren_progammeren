altijd = 0
vaak = 1
regelmatig = 2
soms = 3
nooit = 4

#gekregen
STUDIEDOKTER_TITEL = '''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
'''
OPTIES = f"Kies {altijd}]: altijd; {vaak}: vaak; {regelmatig}: regelmatig; {soms}: soms; {nooit}: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'

COMPETENTIE_ADVIES_TITEL = '''
*********************** STUDIEADVIES ***********************'''
COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''

#zelf gemaakt
print(STUDIEDOKTER_TITEL)
print(OPTIES)
print()

#store point
aantal_weken_vraag = int(input(AANTAL_WEKEN_VRAAG))
competentie_1 = int(input(COMPETENTIE_STELLING_1))
competentie_2 = int(input(COMPETENTIE_STELLING_2))
competentie_3 = int(input(COMPETENTIE_STELLING_3))
competentie_4 = int(input(COMPETENTIE_STELLING_4))
competentie_5 = int(input(COMPETENTIE_STELLING_5))

#weken
if aantal_weken_vraag >= 10:
    competentie_6 = int(input(COMPETENTIE_STELLING_6))
    competentie_7 = int(input(COMPETENTIE_STELLING_7))
else:
    competentie_6 = competentie_7 = 4

#count
altijd = 0
vaak = 1
regelmatig = 2
soms = 3
nooit = 4

countzorg = competentie_1 <= vaak and competentie_2 <= vaak and competentie_3 <= vaak and competentie_4 <= vaak and competentie_5 <= vaak and competentie_6 <= vaak and competentie_7 <= vaak
counttwijfel = competentie_1 <= regelmatig and competentie_2 <= regelmatig and competentie_3 <= regelmatig and competentie_4 <= regelmatig and competentie_5 <= regelmatig and competentie_6 <= regelmatig and competentie_7 <= regelmatig

#advies
print(COMPETENTIE_ADVIES_TITEL)
gemiddelde_score = (competentie_1 + competentie_2 + competentie_3 + competentie_4 + competentie_5 + competentie_6 + competentie_7) / 7 
if gemiddelde_score <= 2 or countzorg:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
if gemiddelde_score <= 3 or counttwijfel:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
