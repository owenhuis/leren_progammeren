#waardes invoeren
a = int(input('welk heel getal wil je hebben?  '))
b = int(input('welk tweede hele getal wil je?  '))
#a groter dan b
if a > b:
    maxwaarde = a
    print(f'{a} = het groostste getal!')
    print(f'de max waarde is {maxwaarde}')
#b groter dan a
elif a < b:
    minwaarde = a
    print(f'{a} is het kleinste getal!')
    print(f'de min waarde = {minwaarde}')
# a en b zijn gelijk
else:
    print(f'{a} = gelijk aan {b}!')
    minwaarde = {a}
    maxwaarde = {b}
    print(f'het maximum getal = {maxwaarde}')
    print(f'het mininum getal = {minwaarde}')
