def get_info() -> dict:
    while True:
        naam_en_leeftijd_dict = {}
        naam_en_leeftijd_dict["name"] = input("Geef een naam: ")
        if naam_en_leeftijd_dict["name"] == "stop":
            break
        naam_en_leeftijd_dict["city"] = input("Geef een straat of stad/dorp naam: ")
        naam_en_leeftijd_dict["age"] = int(input("Geef een leeftijd: "))
        return naam_en_leeftijd_dict
    return naam_en_leeftijd_dict



def get_name_and_age(aantal_personen):
    lijst = []
    for i in range(aantal_personen):
        informatie = get_info()
        lijst.append(informatie)
    return lijst