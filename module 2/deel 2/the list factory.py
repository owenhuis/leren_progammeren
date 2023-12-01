the_list = [] #moet een 3 lijsten met lijst 1 3 getallen (1,2,3) lijst 2 (2,4,6,8) lijst 3 (3,6,9,12,15,18)

hoeveel_lijstjes = input('hoeveel lijstjes wil je?')

if hoeveel_lijstjes == '1':
    nummer_lijst_1 = int(input('hoeveel getallen wil je in je lijstje?')) 
    lijst_1 = list(range(1, nummer_lijst_1 + 1))
    the_list.append(lijst_1)

elif hoeveel_lijstjes == '2':
    nummer_lijst_1 = int(input('hoeveel getallen wil je in je lijstje?'))
    nummer_lijst_2 = int(input('hoeveel getallen wil je in je lijstje?'))
    lijst_1 = list(range(1, nummer_lijst_1 + 1))
    lijst_2 = list(range(2, 2 * nummer_lijst_2 + 1, 2))
    the_list.append(lijst_1)
    the_list.append(lijst_2)

elif hoeveel_lijstjes == '3':
    nummer_lijst_1 = int(input('hoeveel getallen wil je in je lijstje?'))
    nummer_lijst_2 = int(input('hoeveel getallen wil je in je lijstje?'))
    nummer_lijst_3 = int(input('hoeveel getallen wil je in je lijstje?'))
    lijst_1 = list(range(1, nummer_lijst_1 + 1))
    lijst_2 = list(range(2, 2 * nummer_lijst_2 + 1, 2))
    lijst_3 = list(range(3, 3 * nummer_lijst_3 + 1, 3))
    the_list.append(lijst_1)
    the_list.append(lijst_2)
    the_list.append(lijst_3)

print(the_list)