def get_hoi (loop,aantal):
    lijst = []
    for i in range(loop):
        blub = f'hello from function town {aantal}\n'
        lijst.append(blub)
    return lijst
aantal_hallos = int(input('hoevaak wil je hoi '))
stapgroote = 2
aantal =  stapgroote

for a in range(0,aantal_hallos,1):
    hoi = get_hoi(aantal_hallos,aantal)
    aantal += stapgroote
for a in hoi:
    print(hoi)