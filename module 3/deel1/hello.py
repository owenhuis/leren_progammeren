def get_hoi (aantal):
    return print(f'hello from function town{aantal +1}\n')

aantal_hallos = int(input('hoevaak wil je hoi'))

for i in range(aantal_hallos):
    hoi = get_hoi(i)
    