PRIJS_PER_5MIN_VIP = 0.37 #per 5 min of per VIP_PRIJS_PERIODE
VIP_PRIJS_PERIODE = 5
vip_prijs_per_minuut = PRIJS_PER_5MIN_VIP / VIP_PRIJS_PERIODE
dag_ticket_pp = 7.45


hoeveel_ticket = int(input('hoeveel tickets wil je kopen? '))

prijs_ticket = dag_ticket_pp * hoeveel_ticket

vip = input('wil je naar de vip? (ja/nee)  ')
aantal_vip = int(input('hoeveel mensen gaan in de vip?  '))
hoelang_vip = int(input('hoelang wil je gebruik maken van de vip ruimte? (in minuten)   '))
prijs_voor_de_vip = vip_prijs_per_minuut * hoelang_vip * aantal_vip
totale_prijs = dag_ticket_pp + prijs_voor_de_vip

print(f'Dit geweldige dagje-uit met {hoeveel_ticket} mensen in de Speelhal met {hoelang_vip} minuten VR kost je maar {totale_prijs} euro')