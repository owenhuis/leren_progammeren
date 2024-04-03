def check_even(cijfer:int) -> bool: #return true als even return false als oneven
    return cijfer % 2 == 0

def get_omgekeerde_zin(zin:str) -> str: # draait je zin om
    gespleten_string = zin.split()
    omgekeerde_woordenlijst = gespleten_string[::-1]
    gejoinde_string = ' '.join(omgekeerde_woordenlijst)
    return gejoinde_string

def get_aantal_unieke_letters_in_string(meegegeven_string:str) -> int: # geeft je de unieke letters in je string
    unieke_letters_dict = set(meegegeven_string)
    aantalk_unieke_letters = len(unieke_letters_dict)
    return aantalk_unieke_letters

def get_gemiddelde_lengte_woorden(megegeven_str:str) -> float:
    gespleten_string = megegeven_str.split()
    aantal_woorden = 0

    for woord in gespleten_string:
        aantal_woorden += len(woord)
        print(aantal_woorden)

    gemiddelde_lengte_woorden = aantal_woorden / len(gespleten_string)
    return gemiddelde_lengte_woorden

def get_tafel(meegegeven_int:int, nummer_tien:int=10) -> None:
    for linker_getal_in_som in range(1, nummer_tien+1):
        berekening = linker_getal_in_som * meegegeven_int
        print(f'{linker_getal_in_som} x {meegegeven_int} = {berekening}')


