gastheer = True
gasten = True
drank = True
chips = True

if chips and drank and gasten and gastheer:
    print('Start the Party')
elif not gastheer:
    print('No Party')
elif not drank:
    print("party can't start")
elif not (gasten or gastheer):
    print("party can't start")
elif gastheer and drank and not chips:
    print('start the party')
elif gastheer or (gasten and drank and chips):
    print('start the party')
