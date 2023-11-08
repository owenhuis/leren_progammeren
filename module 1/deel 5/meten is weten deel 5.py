#voor de result in hub en de test werkend maken
from math_operations import even, een_groter, twee_groter
from test_lib import test,report
#waardes invoeren

getal1 = input('welk getal wil je hebben?')
getal2 = input('welk getal wil je hebben?')
#gelijk
def vergelijk (getal1: float, getal2: float) -> str:
    if getal1 == getal2:
        return 'Beide getallen zijn even groot'
    elif getal1 > getal2:
        return  f'Maximum: {getal1} en minimum: {getal2}'
    else:
        return  f'Maximum: {getal2} en minimum: {getal1}'

resultaat = vergelijk(getal1, getal2)

print(resultaat)