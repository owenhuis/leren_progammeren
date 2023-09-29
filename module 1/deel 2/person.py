naam = input('wat is je naam?  ')
adres = input('wat is je adres?  ')
postcode = input('wat is je postcode?  ')
woonplaats = input('waar woon je?  ')

adreskaart = f""""
    ----------------------------------------------------
    |  Naam      : {naam}                
    |  Adres     : {adres}            
    |  Postcode  : {postcode}                          
    |  Woonplaats: {woonplaats}                          
    ----------------------------------------------------
"""
print(adreskaart)