import random

#shuffle functie
def get_new_woord(woord) -> str:
    # Zet de string om naar een lijst van karakters
    char_list = list(woord)
    # Shuffle de lijst
    random.shuffle(char_list)
    # Zet de lijst weer terug naar een string
    shuffled_string = ''.join(char_list)
    return shuffled_string



#alle figuren
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k	', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nummers = ['1','2','3','4','5','6','7','8','9','0']
speciale_tekens = ['@', '#', '$', '%', '&' '_', '?']

#alle counts
hoofdletter_count = 0
kleine_letter_count = 0
nummer_count = 0
speciaal_teken_count = 0
combinatie = False
woord_count = 0

#woord
woord = ''


#assemle woord
while combinatie == False:
    hoofdletter_count = 0
    kleine_letter_count = 0
    nummer_count = 0
    speciaal_teken_count = 0
    combinatie = False
    woord_count = 0
    while len(woord) < 24:
        if hoofdletter_count < 6:
            woord += random.choice(letters).capitalize()
            hoofdletter_count += 1
        if speciaal_teken_count < 4:
            woord += random.choice(speciale_tekens)
            speciaal_teken_count += 1
        if nummer_count < 7:
            woord += str(random.choice(nummers))
            nummer_count += 1
        if kleine_letter_count < 8:
            woord += random.choice(letters)
            kleine_letter_count += 1
    print(woord)
    if (' ' in woord or  speciaal_teken_count > 3) and len(woord) == 24:
        woord = ''
        woord_count += 1
        combinatie = False
    if (hoofdletter_count == 6 and kleine_letter_count == 8 and 
        nummer_count == 7 and speciaal_teken_count == 3 and 
        len(woord) == 24):
        combination = True
    else:
        woord_count += 1
    
    if len(woord) == 0:
        pass
    else:
        break

    print(woord)

print(woord)
print(woord_count)
print(len(woord))