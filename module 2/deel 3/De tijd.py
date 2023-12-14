tijd = 24
uur = 0
while uur != tijd:
    uur += 1
    if uur < 12:
        print(uur,'AM')
    elif uur == 24:
        print(uur - 24, 'AM')
    elif uur == 12:
        print(uur, 'PM')
    else:
        print(uur - 12,'PM')