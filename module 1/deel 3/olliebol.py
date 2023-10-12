PRIJS_OLLIEBOL = 99
PRIJS_ZAK_OLLIEBOL = 750
PRIJS_APPELFLAP = 149
AANTAL_OLLIEBOLLEN = 44
AANTAL_APPELFLAP = 2

aantal_zak_olliebol = AANTAL_OLLIEBOLLEN // 10
aantal_olliebollen = AANTAL_OLLIEBOLLEN % 10

prijs_olliebol = aantal_zak_olliebol * PRIJS_ZAK_OLLIEBOL + aantal_olliebollen * PRIJS_OLLIEBOL
prijs_appelflap = AANTAL_APPELFLAP * PRIJS_APPELFLAP
totaal = prijs_appelflap + prijs_olliebol
totaal_euro = totaal / 100

print(f"De {AANTAL_OLLIEBOLLEN} olliebollen en {AANTAL_APPELFLAP} appelflappen kosten: €{totaal_euro}")
