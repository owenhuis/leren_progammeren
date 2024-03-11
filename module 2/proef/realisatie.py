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
print(namen_lijst)

lootjes = namen_lijst.copy()
print(lootjes)

random.shuffle(lootjes)
print(lootjes)
# for item1, item2 in zip(namen_lijst,lootjes):
#     print(item1,item2)
# while any(lootje == naam_lootje for  naam_lootje, lootje in zip(namen_lijst, lootjes)):
#     print('test')
#     random.shuffle(lootjes)
#     print(lootjes)

for blub in namen_lijst, lootjes:
        if blub == blub:
            print('test23233')
            random.shuffle(lootjes)
            print(blub)
            #nu stoppen
        else:
             print('blub')
             #nu moet hij herhalen

for getrokke_lootje in range(len(namen_lijst)):
    print(namen_lijst[getrokke_lootje], 'heeft', lootjes[getrokke_lootje])