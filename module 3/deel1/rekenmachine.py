from functions import *
from time import sleep


first_round = True
while True:
    print('wat wilt u doen? ')
    sleep(.5)
    print('a) optellen')
    print('b) aftrekken')
    print('c) vermenigvuldigen')
    print('d) delen')
    print('e) ophogen')
    print('f) verlagen')
    print('g) verdubbelen')
    print('h) halveren')
    print('i) quit')
    sleep(.5)
    print('kies: ')
    kies = input().lower()
    
    if kies == 'i':
        break
    if first_round == True:
        print('getal 1 : ')
        getal1 = int(input())
        first_round = False
    if kies == 'a':
        print('optellen')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        getal2 = int(input())
        getal1 = get_addition(getal1, getal2)
    elif kies == 'b':
        print('aftrekken')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        getal2 = int(input())
        getal1 = get_subtraction(getal1, getal2)
    elif kies == 'c':
        print('vermenigvuldigen')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        getal2 = int(input())
        getal1 = get_multiplication(getal1, getal2)
    elif kies == 'd':   
        print('delen')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        getal2 = int(input())
        if getal1 != 0 or getal2 != 0:
            getal1 = get_division(getal1, getal2)
        else:
            print('delen is niet mogelijk')
            print('kies opnieuw')
    elif kies == 'e':
        getal2 = 1
        print('ophogen')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        print(getal2)
        getal1 = get_addition(getal1, getal2)
    elif kies == 'f':
        getal2 = 1
        print('verlagen')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        print(getal2)
        getal1 = get_subtraction(getal1, getal2)
    elif kies == 'g':
        getal2 = 2
        print('verdubbelen')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        print(getal2)
        getal1 = get_multiplication(getal1, getal2)
    elif kies == 'h':
        getal2 = 2
        print('halveren')
        print('getal 1 : ')
        print(getal1)
        print('getal 2 : ')
        print(getal2)
        getal1 = get_division(getal1, getal2)
    print('----ANTWOORD----')
    print(getal1)
    sleep(1)



print('-----final answer-----')
print(getal1)