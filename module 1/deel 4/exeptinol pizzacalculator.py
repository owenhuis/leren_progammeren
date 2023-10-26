# Prijzen van de pizza
small_pizza_prijs = 10.99
medium_pizza_prijs = 13.99
large_pizza_prijs = 16.99

# Hoeveelheid pizza's
try:
    pizza_small_count = int(input("Hoeveel small pizza's wil je? "))
    pizza_medium_count = int(input("Hoeveel medium pizza's wil je? "))
    pizza_large_count = int(input("Hoeveel large pizza's wil je? "))
except ValueError:
    print('Voer een geldig getal in')
else:       
    # Bereken de prijs individueel
    pizza_small_price = small_pizza_prijs * pizza_small_count
    pizza_medium_price = medium_pizza_prijs * pizza_medium_count
    pizza_large_price = large_pizza_prijs * pizza_large_count

    # Eindprijs
    totaal_bedrag = pizza_small_price + pizza_medium_price + pizza_large_price

    # Bonnetje
    print("\n-----------------------------")
    print(f"Aantal small pizza's: {pizza_small_count}")
    print(f"Aantal medium pizza's: {pizza_medium_count}")
    print(f"Aantal large pizza's: {pizza_large_count}")
    print("-----------------------------")
    print(f"Totale prijs: {totaal_bedrag:.2f} euro")
    print("-----------------------------")
    print()

