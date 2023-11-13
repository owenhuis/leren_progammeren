import math
#from math_operations import calculate_cilinder_content
from test_lib import test, report

def calculate_cilinder_content (diameter: float, hoogte: float) -> float:
  return round( (diameter / 2) * (diameter / 2) * math.pi * hoogte, 1)


#function 1
#opdracht 1
diameter = 8.0
height = 5.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content)

#opdracht 2
diameter = 11.0
height = 7.0
expect_content = 665.2
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

#opdracht 3
diameter = 18.0
height = 7.0
expect_content = 1781.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content)

#opdracht 4
diameter = 15.0
height = 2.0
expect_content = 353.4
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

#opdracht 5
diameter = 0.0
height = 6.0
expect_content = 0.0
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )
report()

#functie 2
def afronden (getal1 : float,) -> float:
  berekening = round(getal1 * 100 / 5) * 5 / 100
  return round(berekening, 2)



#opdracht1
getal1 = 62.60
expect_content = 62.60
calculated_content = afronden(getal1)
name =f'huidige prijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 2
getal1 = 76.61
expect_content = 76.60
calculated_content = afronden(getal1)
name =f'huidige prijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 3
getal1 = 28.82
expect_content = 28.80
calculated_content = afronden(getal1)
name =f'huidige prijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 4
getal1 = 2.23
expect_content = 2.25
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 5
getal1 = 28.34
expect_content = 28.35
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 6
getal1 = -42.85
expect_content = -42.85
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 7
getal1 = 31.06
expect_content = 31.05
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 8
getal1 = -138.47
expect_content = -138.45
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 9
getal1 = 14.88
expect_content = 14.90
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

#opdracht 10
getal1 = 149.69
expect_content = 149.70
calculated_content = afronden(getal1)
name =f'houdige pprijs: {getal1} verwachte prijs: {expect_content}'
test(name,expect_content, calculated_content)

report()

#functie 3

month_discount_brands = ['vespa','kymco','yamama']
brand = input('kies uit : vespa, kymco, yamama, Aprilia, NIU:  ')
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
  # return calculated discount based on price and brand
    if brand in month_discount_brands:
      return float(round(price * MONTH_DISCOUNT_PERC / 100, 2))
    else:
       return price

price = 599.99
korting_berekenen = round(price * MONTH_DISCOUNT_PERC / 100, 2)


result = calc_discount(price, brand, month_discount_brands)
expect_content = korting_berekenen

name = f'korting op scooter: €{round(korting_berekenen, 2)} als het korting heeft'
test(name,expect_content, result)

report()