try:
    leeftijd = int(input("wat is je leeftijd?  "))
except ValueError:
    print("voer een geldig getal in")
else:
    print(f"je bent dan {leeftijd} oud")