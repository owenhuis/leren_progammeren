from collections import Counter
import math, random


def get_gemiddelde(getal1,getal2):
    return getal1 / getal2

def get_eerste_item (getallen):
    return getallen[0]

def get_kleinste (getal1,getal2):
    return getal1 / getal2

def get_grootste (getal1,getal2):
    return getal1 / getal2

def get_unieke_getallen (getallen_lijst):
    return list(set(getallen_lijst))

def tel_element_aantal (getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

def get_deelbaar_1 (unieke_getallen):
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbaar1

def get_deelbaar_2 (unieke_getallen):
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return deelbaar2

def get_position (getallen):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def check_if_in (getallen):
    return controlegetal1 in getallen and controlegetal2 in getallen

def get_afwijking(gemiddelde, getallen, aantal):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking
def get_random_number (getallen, aantal):
    return getallen[random.randint(0,aantal-1)]
def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    # Gemiddelde berekenen
    aantal = len(getallen)

    # Som van alle getallen in de lijst
    som = sum(getallen)

    # Gemiddelde berekenen
    gemiddelde = get_gemiddelde(som,aantal)

    # Het grootste getal in de lijst
    grootste_getal = max(getallen)
    
    # Het kleinste getal in de lijst
    kleinste_getal = min(getallen)
    
    # Het eerste getal in de lijst
    eerste_getal = get_eerste_item(getallen)
    
    # Het kleinste getal gedeeld door het eerste controle getal
    delen1 = get_kleinste(kleinste_getal,controlegetal1)

    # Het grootste getal gedeeld door het tweede controle getal
    delen2 = get_grootste(grootste_getal,controlegetal2)

    # alle unieke getallen
    unieke_getallen = get_unieke_getallen(getallen)

    # Aantal unieke elementen in de lijst
    aantal_unieke_elementen = len(unieke_getallen)

    # Verschil tussen aantal unieke elementen en eerste controle getal
    verschil1 = abs(aantal_unieke_elementen - controlegetal1)

    # Sorteer de lijst van getallen
    gesorteerde_lijst = sorted(getallen)

    # Sorteer de lijst van unieke getallen
    gesorteerde_lijst_uniek = sorted(unieke_getallen)

    # Tel het aantal keren dat elk uniek element voorkomt in de lijst
    telling_elementen = tel_element_aantal(getallen)
    
    # Getallen die deelbaar zijn door het eerste controlle getal
    deelbaar1 = get_deelbaar_1(unieke_getallen)

    # Getallen die deelbaar zijn door het tweede controlle getal
    deelbaar2 = get_deelbaar_2(unieke_getallen)

    # Controleer of een bepaald getallen in de lijst voorkomen
    komtvoor = check_if_in(getallen)

    # Vindt de posities van heteerste controle getal
    posities = get_position(getallen)

    # Standaardafwijking berekenen
    
    standaardafwijking = get_afwijking(gemiddelde, getallen, aantal)

    # Shuffle de lijst
    random.shuffle(getallen)

    # Pak een random getal uit de lijst
    random_getal = get_random_number(getallen, aantal)

    # Verschil tussen twee getallen
    verschil2 = abs(random_getal - controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Som": som,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")