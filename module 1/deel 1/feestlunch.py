#feestlunch

#prijs/waarde van alles
croissantjes_prijs = .39
stokbrood_prijs = 2.78
kortingsbon_waarde = .50

#input van hoeveel je van alles heb
hoeveel_croissantjes = int(input('hoeveel croissantjes wil je?  '))
hoeveel_stokbrood = int(input('hoeveel stokbrood wil je?  '))
kortingsbon_hoeveelheid = int(input('hoeveel kortingsbonnen heeft u?  '))

#prijs van alles
croissantjes = hoeveel_croissantjes* croissantjes_prijs
stokbrood = stokbrood_prijs* hoeveel_stokbrood
kortingsbon = kortingsbon_hoeveelheid * kortingsbon_waarde

#totale prijs
totaal_bedrag = croissantjes + stokbrood - kortingsbon

#de eind print
print(f'De feestlunch kost je bij de bakker {totaal_bedrag} euro voor de {hoeveel_croissantjes} croissantjes en de {hoeveel_stokbrood} stokbroden als de {kortingsbon_hoeveelheid} kortingsbonnen nog geldig zijn!')