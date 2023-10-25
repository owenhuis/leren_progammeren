#prijzen van de pizza
small_pizza_prijs  = 10.99 
medium_pizza_prijs = 13.99 
large_pizza_prijs  = 16.99 

#hoeveelheid pizza's
pizza_small =  int(input("hoeveel small pizza's wil je ?  "))
pizza_medium = int(input("hoeveel medium pizza's wil je?  "))
pizza_large =  int(input("hoeveel large pizza's wil je?   "))

#pizza's prijs individueel
pizza_1 =  small_pizza_prijs * pizza_small
pizza_2 = medium_pizza_prijs * pizza_medium
pizza_3 =  large_pizza_prijs * pizza_large

#eindpreis
totaal_bedrag = pizza_1 + pizza_2 + pizza_3

#bonnetje
print()
print()
print("-----------------------------")
print(f" Aantal small pizza's: {pizza_small}   ")
print(f" Aantal medium pizza's: {pizza_medium}  ")
print(f" Aantal large pizza's: {pizza_large}   ")
print("-----------------------------")
print(f" Totaalbedrag: {totaal_bedrag:.2f} euro  ")
print("-----------------------------")
print()
print()