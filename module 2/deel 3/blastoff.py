import time
getal = 30
while getal > 0:
    print(getal)
    getal -= 1
    time.sleep(1)
    if getal == 0:
        print(0)
        time.sleep(1)
        print('blastoff')