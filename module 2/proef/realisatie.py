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
print('namen lijst',namen_lijst)

lootjes = namen_lijst.copy()
print('lootjes lijst',lootjes)

random.shuffle(lootjes)
print('eerste shuffle',lootjes)

verloten = True
counter = 0
while verloten:
    for blub in range(len(namen_lijst)):
        if namen_lijst[blub] == lootjes[blub]:
            print(f'{blub +1 } is gelijk')
            random.shuffle(lootjes)
            print('shuffle ',lootjes)
            counter = 0
        else:
            print(f'klopt {blub +1} van de list')
            counter += 1
            if counter == len(namen_lijst):
                verloten = False
                break
            #nu stoppen

for getrokke_lootje in range(len(namen_lijst)):
    print(namen_lijst[getrokke_lootje], 'heeft', lootjes[getrokke_lootje])