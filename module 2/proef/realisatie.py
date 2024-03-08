import random

namen_lijst = []

namen_toevoegen = True


while namen_toevoegen:
    naam = input('wie doet er mee met lootje trekken? ').lower()
    if naam not in namen_lijst:
        namen_lijst.append(naam)
    namen_lijst_tellen = len(namen_lijst)
    if namen_lijst_tellen >= 3:
        nog_een = input('wil je nog een naam toevoegen? (ja/nee)')
        if nog_een != 'ja':
            namen_toevoegen = False
# print(namen_lijst)

lootje = namen_lijst.copy()
# print(lootje)

random.shuffle(lootje)
# print(lootje)

while lootje == namen_lijst:
    # print('test')
    random.shuffle(lootje)
    # print(lootje)

for getrokke_lootje in range(len(namen_lijst)):
    print(namen_lijst[getrokke_lootje], 'heeft', lootje[getrokke_lootje])