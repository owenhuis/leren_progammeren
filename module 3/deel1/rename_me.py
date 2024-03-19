def get_even_oneven(meegegeven_int:int) -> bool: #return true als even return false als oneven
    return meegegeven_int % 2 == 0

def get_de_zin_van_achter_naar_voor(meegegeven_string:str) -> str: # leest de zin van achter naar voren
    gespleten_string = meegegeven_string.split()
    doldwaze_broccoli = gespleten_string[::1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

def ruimte_hamsterwiel(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')


blub = get_de_zin_van_achter_naar_voor('bluubert kjnfdsncdz popofupij')
print(blub)