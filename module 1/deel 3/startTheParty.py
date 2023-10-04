#variable hoeveelheden
gastheer_naam = input('wat is de naam van de gastheer?  ')
gasten = int(input('hoeveel gasten zijn er?  '))
#waardes true or false
gastheer = True
drank = True
chips = True

if gastheer_naam == 'owen':
    print('start the party')
elif gastheer_naam == 'slemmer':
    print('no party')
elif (not chips and not drank) or (gasten >= 4) or (gasten <= 20) or (gastheer):
    print('Start the Party!')
else:
    print('No Party')
