#dictioneries
# mijn_tuple = ()
# mijn_lijst = [17, 28, 15, 33]

# print(mijn_lijst[1])

# personen_lijst = []
# for _ in range(2):
#     persoon = {}
#     persoon['voornaam'] = input('wat is je voornaam  ')
#     persoon['achternaam'] = input('wat is je achternaam  ')
#     persoon['leeftijd'] = int(input('wat is je leeftijd  '))
#     personen_lijst.append(persoon)

# print(personen_lijst)

auto_lijst = []
for _ in range(2):
    auto = {}
    auto['automerk'] = input('welk merk is je auto?  ')
    auto['model'] = input('welk model is je auto?  ')
    auto['prijs'] = float(input('welke prijs is je auto?  '))
    auto_lijst.append(auto)

for prijs in auto_lijst:
    print(prijs['prijs'])