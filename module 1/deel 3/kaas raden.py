#vraag 1
kaaskleur = input('Is de kaas geel? (ja/nee) ').lower
#linkerzijde
if kaaskleur == 'ja': 
    
    gatenkaas = input('Zitten er gaten in de kaas? (ja/nee) ').lower
    if gatenkaas == 'ja':
        durekaas = input('Is de kaas belachelijk duur? (ja/nee) ').lower
        if durekaas == 'ja':
            # alleen ja klaar
            print('Je kaas = emmenthaler') 
        elif durekaas == 'nee':
            #twee keer ja een keer nee
            print('Je kaas = leerdammer') 
    elif gatenkaas == 'nee':
        hardekaas = input('Is de kaas hard? (ja/nee) ').lower
        if hardekaas == 'ja':
            # ja nee ja
            print('Je kaas = permigiano reggiano') 
        elif hardekaas == 'nee':
            # ja nee nee
            print('Je kaas = goudse kaas')
#rechterzijde
elif kaaskleur == 'nee': 
    schimmelkaas = input('Heeft de kaas blauwe schimmel? (ja/nee) ').lower
    if schimmelkaas == 'ja':
        kaaskorstblauw = input('Heeft de kaas korst? (ja/nee) ').lower
        if kaaskorstblauw == 'ja':
            #nee ja ja
            print('Je kaas = blue deu rochbaron') 
        elif kaaskorstblauw == 'nee':
            #nee ja nee
            print('Je kaas = foume d"ambert') 
    elif schimmelkaas == 'nee':
        kaaskorst = input('Heeft de kaas korst? (ja/nee) ').lower
        if kaaskorst == 'ja':
             #nee nee ja
            print('Je kaas = camembert')
        elif kaaskorst == 'nee':
            #nee nee nee
            print('Je kaas = mozzarella')
