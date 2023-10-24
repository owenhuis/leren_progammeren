DOOS_12 = 12
DOOS_10 = 10
DOOS_6 = 6
aantal_eiren = int(input("hoeveeleieren moet ik verpakken?   "))


dozen_12 = aantal_eiren // DOOS_12
print(f'{dozen_12} doos/zen van 12')
rest = aantal_eiren - dozen_12 * DOOS_12
print(f'{rest} eien zijn over van 12 dozen')
doos_10 = rest // DOOS_10
print(doos_10)
rest = aantal_eiren - doos_10 * DOOS_10 
dozen_6 = rest // DOOS_6
print(f'{dozen_6} doos/zen van 6')
rest = rest - dozen_6 * DOOS_6
print(f'{rest} eieren zijn over van doos van 6')
if rest >= 1:
    dozen_6 += 1
totaal_aantal_eieren = dozen_12 + dozen_6 + rest
print(f'{totaal_aantal_eieren} dozen eieren heb je in totaal')