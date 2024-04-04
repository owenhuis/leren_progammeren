def get_name_and_age_and_adress(aantal_personen):
    lijst = []
    for i in range(aantal_personen):
        naam_en_leeftijd_dict = {}
        naam_en_leeftijd_dict["name"] = input("Geef een naam: ")
        if naam_en_leeftijd_dict["name"] == "stop":
            break
        naam_en_leeftijd_dict["city"] = input("Geef een adres: ")
        naam_en_leeftijd_dict["age"] = int(input("Geef een leeftijd: "))
        lijst.append(naam_en_leeftijd_dict)
    return lijst

hoeveel_personen = int(input("Geef het aantal personen: "))
naam_en_leeftijd = get_name_and_age_and_adress(hoeveel_personen)

for i in naam_en_leeftijd:
    print(i["name"],', die in ',i["city"],'woont,', 'is', i["age"], 'jaar')