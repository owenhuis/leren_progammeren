from functietester import *

def get_apppelmoes(woord) -> str:
    if woord == "appel":
        return 'appelmoes'
    else:
        return 'hier kan ik geen appelmoes van maken'
    
def get_chocola(woord) -> str:
    if woord == "chocola":
        return 'chocola lekker'
    else:
        return 'gesmolten :_('


verwacht = "apppel"
resultaat = get_apppelmoes
handle_test(naam_test='appel', verwacht= 'appel', resultaat='appelmoes')

verwacht = "chocola"
resutlaat = get_chocola
handle_test(naam_test='chocola',verwacht= 'chocola', resultaat= 'chocola lekker')