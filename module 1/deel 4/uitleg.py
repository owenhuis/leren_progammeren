def bereken_btw(bedrag: float) -> float: # parameter
    bedrag_inc = bedrag_inc * 1.21
    return bedrag_inc


bedrag_ex = 100
bedrag_inc = bereken_btw(bedrag_ex)
bedrag_incl = bereken_btw(50.00)

print(bedrag_inc)
print(bedrag_incl)