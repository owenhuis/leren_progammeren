croissantjes = 0.39
stokbrood = 2.78
kortingsbon = 0.50

hoeveel_croissantjes = int(input('hoeveel croissantjes wil je?  '))
hoeveel_stokbrood = int(input('hoeveel stokbrood wil je?  '))
kortingsbon_hoeveelheid = int(input('hoeveel kortingsbonnen heeft u?  '))
totaal_bedrag = hoeveel_croissantjes * croissantjes + stokbrood * hoeveel_stokbrood - kortingsbon_hoeveelheid * kortingsbon
print(f'uw totaalbedrag = {totaal_bedrag}')