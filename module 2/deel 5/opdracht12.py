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

def get_name (fruit):
    return len(fruit['name'])

langste_fruitnaam = max(fruitmand, key=get_name) # voor langste naam

naam_letters = get_name(langste_fruitnaam) # voor aantal letters
naam_kleur = kleur.get(langste_fruitnaam['color'], langste_fruitnaam['color']) # voor kleuren

print(f'de "{langste_fruitnaam["name"]}" ({naam_letters} letters) heeft een {naam_kleur} kleur en een gewicht van {langste_fruitnaam["weight"] / 1000} kg')