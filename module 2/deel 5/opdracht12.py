from fruitmand import *

kleur = {
    'yellow': 'gele',
    'green': 'groene',
    'orange': 'oranje',
    'red': 'rode',
    'brown': 'bruine',
    'black': 'zwarte',
    'pink': 'roze',
    'purple': 'paarse'
}


tekst = max(fruitmand, key=lambda x: len(x["name"])) # voor langste naam

naam_letters = len(tekst['name']) # voor aantal letters
naam_kleur = kleur.get(tekst['color'], tekst['color']) # voor kleuren

print(f'de "{tekst["name"]}" ({naam_letters} letters) heeft een {naam_kleur} kleur en een gewicht van {tekst["weight"] / 1000} kg')