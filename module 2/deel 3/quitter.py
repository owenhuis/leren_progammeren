count = 0
answer = input('?').lower()
while answer != 'quit':
    count += 1
    answer = input('?').lower()
    if answer == 'quit':
        break

print('aantal keer gefaald: ',count)