import random
namen_lijst = ['jan']
lootjes = namen_lijst.copy()


for i in range(20):
    while True:
        for teller in range(len(namen_lijst)):
            if namen_lijst[teller] == lootjes[teller]:
                print(f'{teller +1 } is gelijk')
                random.shuffle(lootjes)
                print('shuffle ',lootjes)
                print(teller)
                break
        if namen_lijst[teller] != lootjes[teller]:
            break

while len(namen_lijst) > 0:
    naam_weten = input('wie wilt zijn lootje weten?  ')
    for getrokke_lootje in range(len(namen_lijst)):
        if naam_weten == namen_lijst[getrokke_lootje]:
            print(namen_lijst[getrokke_lootje], 'heeft', lootjes[getrokke_lootje])
            namen_lijst.remove(naam_weten)
            # print(namen_lijst)
            break