def get_name_and_age(aantal_personen):
    lijst = []
    for i in range(aantal_personen):
        naam_en_leeftijd_dict = {}
        naam_en_leeftijd_dict["name"] = input("Geef een naam: ")
        if naam_en_leeftijd_dict["name"] == "stop":
            break
        naam_en_leeftijd_dict["age"] = int(input("Geef een leeftijd: "))
        lijst.append(naam_en_leeftijd_dict)
    return lijst

hoeveel_personen = int(input("Geef het aantal personen: "))
naam_en_leeftijd = get_name_and_age(hoeveel_personen)

for i in naam_en_leeftijd:
    print(i["name"], i["age"])