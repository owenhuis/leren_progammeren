WEEKDAGEN = 'maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag'


print(','.join(WEEKDAGEN))
print()
for werkdagen in WEEKDAGEN[:5]:
    print(werkdagen, end=' ')
print()
for weekenddagen in WEEKDAGEN[5:]:
    print(weekenddagen, end=' ')
print()
for omgekeerd in reversed(WEEKDAGEN):
    print(omgekeerd, end=' ')
print()
for omgekeerd_werk in reversed(WEEKDAGEN[:5]):
    print(omgekeerd_werk, end=' ')
print()
for omgekeerd_weekend in reversed(WEEKDAGEN[5:]):
    print(omgekeerd_weekend, end=' ')