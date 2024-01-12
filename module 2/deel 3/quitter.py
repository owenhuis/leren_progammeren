count = 0
answer = ''
while answer != 'quit':
    answer = input('?').lower()
    if answer == 'quit':
        break
    count += 1

print('aantal keer gefaald: ',count)