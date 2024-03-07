import random



namen = ['a','b','c']
copie = namen.copy()

for naam in namen:
    lootje = random.shuffle(copie)
    print('test')
    print(lootje)
    while namen == lootje:
        keuze1 = random.shuffle(copie)
        print(keuze1)
    
