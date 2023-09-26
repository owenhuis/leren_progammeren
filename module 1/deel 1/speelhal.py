dag_ticket_pp = 7.45


hoeveel_ticket = int(input('hoeveel tickets wil je kopen? '))

prijs_ticket = dag_ticket_pp * hoeveel_ticket

vip = input('wil je naar de vip? (ja/nee)  ')
if vip == 'ja':
    aantal_vip = int(input('hoeveel mensen gaan in de vip?  '))
    hoelang_vip = int(input('hoelang wil je gebruik maken van de vip ruimte? (in minuten)   '))
    tijd_in_de_vip = 0.37 * hoelang_vip * aantal_vip
    print(f'uw totaal bedrag = {dag_ticket_pp * hoeveel_ticket + tijd_in_de_vip * aantal_vip}')
elif vip == 'nee':
    print(f'uw totaal bedrag = {prijs_ticket} ')