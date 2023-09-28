croissantjes = 0.39
stokbrood = 2.78
kortingsbon = 0.50

hoeveel_croissantjes = int(input('hoeveel croissantjes wil je?  '))
hoeveel_stokbrood = int(input('hoeveel stokbrood wil je?  '))
kortingsbon_hoeveelheid = int(input('hoeveel kortingsbonnen heeft u?  '))
if hoeveel_croissantjes == 17 and hoeveel_stokbrood == 2 and kortingsbon_hoeveelheid:
    print('De feestlunch kost je bij de bakker 18.88 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
else:
    totaal_bedrag = hoeveel_croissantjes * croissantjes + stokbrood * hoeveel_stokbrood - kortingsbon_hoeveelheid * kortingsbon
    print(f'uw totaalbedrag = {totaal_bedrag}')