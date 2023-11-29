#start
print('je zit thuis op de bank tv te kijken dan komt er een swat team binnen wat doe je')
geswat = input('geef op of ga naar je wapen kamer  ')
#linkerzijde
if geswat == 'geef op':
    print('je wordt gevangen gezet voor 50 jaar door je illegale drugs business') 
    tegenstander = input('na 10 jaar komt er iemand in de gevangenis waarvan jij iemand in zijn familie hebt vermoord wat doe je? (vecht/ geef op)  ').lower()
    if tegenstander == 'geef op':
        print('de gaurds deden niks ze mogen je niet.')
        print('je bent doodt op 30 jaar oud') 
    elif tegenstander == 'vecht':
        wapen = input('je tegenstander heeft een mes wat gebruik jij? (nuke/ mes/ shotgun)  ').lower()
        if wapen == 'nuke':
            print('je had een mentaliteit van als ik dood ga gaat iedereen') 
            print('je bent dood op 30 jaar leeftijd')
        elif wapen == 'shotgun':
            print('je rend op een gaurd af pakt zijn shotgun hij probeert je tegen te houden maar je schiet hem neer je draait om en schiet je tegenstander neer')
            print('je ziet een opening en rally iedere gevangene op en gaat vechten')
            print('ondanks je geniale plan ben je geraakt in de cross-fire en bent doodgegegaan op 30 jarige leeftijd')
        elif wapen == 'mes':
            print('jij wordt op een niet fatale plek geraakt je pakt het mes dat in je zit en steekt het in zijn nek en je wint maar je krijgt + 5 jaar ')
            extra_tijd = input('wat doe je (wacht/break-out)').lower
            if extra_tijd == 'wacht':
                print('je bent 75 wanneer je de gevangenis uit komt heel je familie is doodt door een rival clan je kan er niet tegen en je doodt jezelf')
            elif extra_tijd == 'break-out':
                break_out = input('hoe ontsnap je (sneaky/ rally)').lower()
                if break_out == 'rally':
                    print('ondanks je geniale plan ben je geraakt in de cross-fire en bent doodgegegaan op 30 jarige leeftijd')
                elif break_out == 'sneaky':
                    print('het is je gelukt je bent een vrij man de wereld ligt aan je voeten jij mag doen watn je wilt')
                    print()
                    print()
                    print('je hebt gewonnen gefeliciteerd')

#rechterzijde
elif geswat == 'wapen kamer':
    print('jij rent naar je wapenkamer toe jij kan niet naar buiten en zij niet naar binnen wat doe je') 
    vault = input('een val / yolo rush / wacht  ').lower()
    if vault == 'wacht':
        wacht = print('jij wacht en wacht dan krijg je honger en realiseer dat je geen eten hebt en na een paar dagen ga je dood')
    elif vault == 'val':
        code = int(input('je hebt twee knoppen self destruct en fake self destruct maar ze zijn niet gelabeld je moet eerst een code invoeren je weet ze allemaal behalve een, je twijfelt tussen 1 of 3 wat kies je'))
        if code > 2 or code < 2:
           print('de code was fout je bent dood!')
        else:
            print('het was correct maar je hoort een countdown de fbi rent weg maar het is te laat iedereen is doodt')
    elif vault == 'yolo rush':
        print('je rent naar buiten en gooit enge edit course en 200 pumped ze allemaal')
        fbi = input('je hebt ze allemaal gedoood wat doe je nu? (lay low/ wordt populair)').lower()
        if fbi == 'lay low':
            print('het leek je handig om laag te blijven aangezien je nu heel erg gezocht wordt door verschillende gevaarlijke mensen')
            print('het leven werd je te saai dus je dode je zelf')
        elif fbi == 'wordt populair':
            print("je koos om populiar te worden met je actie's")
            print('je buisnnees groede 10000x zo groot en je werdt de grootste drugs lord aller tijden')
            print()
            print()
            print('je hebt gewonnen gefeliciteerd')

print('dit is het einde')