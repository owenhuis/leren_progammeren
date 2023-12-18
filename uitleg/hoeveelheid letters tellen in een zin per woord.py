def add_length(zin):
    woorden_lijst = []
    losse_woorden = zin.split()
    for woord in losse_woorden:
        nieuw_woord = woord
        getal = len(woord)
        woorden_lijst.append(f'{nieuw_woord} {getal}')
    return woorden_lijst

result = add_length('voorbeeld van een zin')

print(result)