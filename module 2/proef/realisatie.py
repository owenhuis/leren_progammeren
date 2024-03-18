import random

namen_lijst = []

namen_toevoegen = True

# namen ophalen / toevoegen
while namen_toevoegen:
    naam = input('wie doet er mee met lootje trekken? ').lower()
    if naam not in namen_lijst:
        namen_lijst.append(naam)
    else:
        print('naam is al gebruikt')
    namen_lijst_tellen = len(namen_lijst)
    if namen_lijst_tellen >= 3:
        nog_een = input('wil je nog een naam toevoegen? (ja/nee)')
        if nog_een != 'ja':
            namen_toevoegen = False
# print('namen lijst',namen_lijst)

#verloten van de namen
lootjes = namen_lijst.copy()
# print('lootjes lijst',lootjes)

random.shuffle(lootjes)
# print('eerste shuffle',lootjes)

while True:
    for teller in range(len(namen_lijst)):
        if namen_lijst[teller] == lootjes[teller]:
            print(f'{teller +1 } is gelijk')
            random.shuffle(lootjes)
            print('shuffle ',lootjes)
            print(teller)
            break
    if namen_lijst[teller] != lootjes[teller]:# als de laatste uit de for ongelijk is dan breakt hij alsnog uit de for en dit stopt dat!
        break

while len(namen_lijst) > 0:
    naam_weten = input('wie wilt zijn lootje weten?  ')
    for getrokke_lootje in range(len(namen_lijst)):
        if naam_weten == namen_lijst[getrokke_lootje]:
            print(namen_lijst[getrokke_lootje], 'heeft', lootjes[getrokke_lootje])
            namen_lijst.remove(naam_weten)
            break