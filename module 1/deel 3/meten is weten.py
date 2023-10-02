a = int(input('welk heel getal wil je hebben?  '))
b = int(input('welk tweede hele getal wil je?  '))

if a >= b:
    maxwaarde = a
    print(f'{a} = het groostste getal!')
    print(f'de max waarde is {maxwaarde}')
elif a <= b:
    minwaarde = a
    print(f'{a} is het kleinste getal!')
    print(f'de min waarde = {minwaarde}')
else:
    print(f'{a} = gelijk aan {b}!')