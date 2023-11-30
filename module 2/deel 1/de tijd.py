for uur in range(1, 25):
    if uur < 12:
        print(uur,'AM')
    elif uur == 24:
        print(uur - 12, 'AM')
    elif uur == 12:
        print(uur, 'PM')
    else:
        print(uur - 12,'PM')