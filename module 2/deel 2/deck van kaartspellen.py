import random
vormen = ['harten', 'klaver', 'schoppen', 'ruiten']
nummers = ['aas',2,3,4,5,6,7,8,9,10,'boer','vrouw','heer']
volle_deck = ['joker','joker']

for vorm in vormen:
    for nummer in nummers:
        kaart = vorm + " " + str(nummer)
        volle_deck.append(kaart)

hand = random.shuffle(volle_deck)
for hand in range(7):
    handje = volle_deck.pop(0)
    print(f'kaart {hand+1}: {handje}')

print('deck (47 kaarten): ', volle_deck)