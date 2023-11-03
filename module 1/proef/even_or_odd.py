def even_or_odd(number):
    if int(number /2):
        return 'Odd'
    else:
        return 'even'
print()
number = int(input("welk nummer wil je testen?"))
antwoord = even_or_odd(number)
print()
print(antwoord)
print()