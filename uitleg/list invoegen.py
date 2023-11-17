naam_lijst = []


while True:
    naam_invoer = input("vooer een naam in    ")
    if naam_invoer.lower() == 'stop':
        break    
    else:
     naam_lijst.append(naam_invoer)

if naam_invoer in naam_lijst:
        print("deze zit er al in")


print("alle namen in de lijst:",naam_lijst)

    