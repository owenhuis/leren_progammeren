from get_name_and_age_and_adress import get_name_and_age

hoeveel_personen = int(input("Geef het aantal personen: "))
naam_en_leeftijd = get_name_and_age(hoeveel_personen)

for i in naam_en_leeftijd:
    print(f'in {i["city"]}, woont de {i["age"]} jarige {i["name"]}')