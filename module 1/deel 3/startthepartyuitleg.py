#variable hoeveelheden
gastheer = input('wat is de naam van de gastheer?  ')
gasten = int(input('hoeveel gasten zijn er?  '))
#waardes true or false
drank = True
chips = True
gatsenok = gasten >= 4 and gasten <= 20

party1 = gatsenok and drank and chips and gastheer != 'slememer'
party2 = gastheer != '' and drank and gastheer != 'slemmer'
party3 = gastheer == 'owen'

if party1 or party2 or party3:
    print('feest gaat door')
else:
    print('de party gaat niet door')




#if gastheer_naam == 'owen':
#    print('start the party')
#elif gastheer_naam == 'slemmer':
 #   print('no party')
#elif (not chips and not drank) or (gasten >= 4) or (gasten <= 20) or (gastheer):
 #   print('Start the Party!')
#else:
#    print('No Party')