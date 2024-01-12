START_GETAL = 50
STOP = 1000
hoeveelheid = START_GETAL
stap = 0

aan_str_toevoegen = f'{START_GETAL}'

while hoeveelheid <= STOP:    
    stap += 1
    stapsgroote = stap + START_GETAL
    hoeveelheid += stapsgroote
    aan_str_toevoegen += f' + {stapsgroote}'

    print(f'{stap}) {aan_str_toevoegen} = {hoeveelheid} ')


