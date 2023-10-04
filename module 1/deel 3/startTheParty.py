#naam gastheer
gastheer_naam = input('wat is de naam van de gastheer?')

#wardes true or false
gastheer = True
gasten = True
drank = True
chips = True

if gastheer_naam == 'owen':
    print('start the party')
elif gastheer_naam == 'slemmer':
    print('no party')
elif (not chips and not drank) or (gasten or gastheer):
    print('Start the Party')
else:
    print('No Party')
