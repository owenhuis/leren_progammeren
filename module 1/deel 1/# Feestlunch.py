# Feestlunch

# Prijs/waarde van alles
croissantjes_prijs = 39  # Prijs in centen
stokbrood_prijs_euro = 278  # Prijs in centen
kortingsbon_waarde = 50  # Waarde in centen

# Input van hoeveel je van alles hebt
hoeveel_croissantjes = int(input('Hoeveel croissantjes wil je?  '))
hoeveel_stokbrood = int(input('Hoeveel stokbroden wil je?  '))
kortingsbon_hoeveelheid = int(input('Hoeveel kortingsbonnen heb je?  '))

# Prijs van alles
croissantjes = hoeveel_croissantjes * croissantjes_prijs
stokbrood = hoeveel_stokbrood * stokbrood_prijs_euro  # Nu in centen
kortingsbon = kortingsbon_hoeveelheid * kortingsbon_waarde

# Totale prijs
totaal_bedrag = croissantjes + stokbrood - kortingsbon

# De eindprint
print(f'De feestlunch kost je bij de bakker {totaal_bedrag} centen voor de {hoeveel_croissantjes} croissantjes en de {hoeveel_stokbrood} stokbroden als de {kortingsbon_hoeveelheid} kortingsbonnen nog geldig zijn!')
