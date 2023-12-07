import random
vormen = ['harten', 'klaveren', 'schoppen', 'ruiten']
nummer = [1,2,3,4,5,6,7,8,9,10,11,12,13]
volle_dek = ['joker','joker']

for dek in range(52):
    #speciale caracters
    if nummer == 11:
        nummer = 'boer'
    elif nummer == 12:
        nummer = 'koningning'
    elif nummer == 13:
        nummer = 'koning'
    elif nummer == 1:
        nummer = 'aas'
    kaart = f'{vormen}  {nummer}'
    volle_dek.append(kaart)
for hand in range(7):
    hand = random.shuffle(volle_dek)
    handje = hand.pop(volle_dek)
    print(handje)
print('deck (47 kaarten): ', volle_dek)