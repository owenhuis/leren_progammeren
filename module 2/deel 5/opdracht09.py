from opdracht01 import *

kleurtje = []

for kleur in fruitmand:
    if kleur['color'] in kleurtje:
        None
    else:
        kleurtje.append(kleur['color'])

print(kleurtje)