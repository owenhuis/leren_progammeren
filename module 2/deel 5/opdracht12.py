from opdracht01 import *

kleur = {
    'yellow': 'gele',
    'green': 'groene',
    'orange': 'oranje',
    'red': 'rode',
    'brown': 'bruine',
}


for tekst in fruitmand:
    naam_letters = len(tekst['name'])
    naam_kleur = kleur.get(tekst['color'], tekst['color'])
    print(f'de "{tekst["name"]}" ({naam_letters} letters) heeft een {naam_kleur} kleur en een gewicht van {tekst["weight"] / 1000} kg')