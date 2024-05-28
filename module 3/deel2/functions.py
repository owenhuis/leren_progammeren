import time
from termcolor import colored
from data import *
import math

##################### O03 #####################

def copper2silver(amount:int) -> float:
    amount = amount / 10
    return amount

def silver2gold(amount:int) -> float:
    amount = amount / 5
    return amount

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    amount = amount * 25
    return amount

def getPersonCashInGold(personCash:dict) -> float:
    amount = 0
    for item in personCash:
        if item == 'copper':
            amount += copper2gold(personCash[item])
        elif item == 'silver':
            amount += silver2gold(personCash[item])
        elif item == 'gold':
            amount += personCash[item]
        elif item == 'platinum':
            amount += platinum2gold(personCash[item])
    return amount

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    kosten = 0
    kosten += people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    kosten += horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    kosten = copper2gold(kosten)
    return round(kosten,2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    items = []
    for item in list:
        if key in item and item[key] == value:
            items.append(item)
    return items

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True) 
    

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    return getAdventuringPeople(getShareWithFriends(friends))

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    totaal_mensen = math.ceil(people/ 2)
    return totaal_mensen

def getNumberOfTentsNeeded(people:int) -> int:
    totaal_mensen = math.ceil(people/3)
    return totaal_mensen

def getTotalRentalCost(horses:int, tents:int) -> float:
    totale_kosten = 0
    paarden_kosten = silver2gold(horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)
    totale_kosten += paarden_kosten
    tenten_kosten = tents * COST_TENT_GOLD_PER_WEEK * round(JOURNEY_IN_DAYS / 7)
    totale_kosten += tenten_kosten
    return totale_kosten

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    counter = len(items)
    text = []
    for item in items:
        name = item['name']
        amount = item['amount']
        unit = item['unit']
        text1 = f'{amount}{unit} {name}'
        text.append(text1)
    return ', '.join(text[:-1]) + f' & {text[-1]}' if counter > 1 else text[0]

def getItemsValueInGold(items:list) -> float:
    total_money = 0
    for item in items:
        price = item['price']
        amount = item['amount']
        if price['type'] == 'copper':
            money = copper2gold(amount *price['amount'])
            total_money += money
        elif price['type'] == 'silver':
            money = silver2gold(amount *price['amount'] )
            total_money += money
        elif price['type'] == 'gold':
            total_money +=  amount *price['amount'] 
        elif price['type'] == 'platinum':
            money = platinum2gold(amount *price['amount']  )
            total_money += money

    return float(total_money)

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_money = 0
    for mens in people:
        total_money += getPersonCashInGold(mens['cash'])
    return float(total_money)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    lijst = []
    for interesting in investors:
        if interesting['profitReturn'] <= 10:
            lijst.append(investors)
    return lijst

def getAdventuringInvestors(investors:list) -> list:
    return getInterestingInvestors(getAdventuringPeople(investors))

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_price = 0.0
    
    adventuring_investors = getAdventuringInvestors(investors)
    aantal_adventuring_investors = len(adventuring_investors)

    if aantal_adventuring_investors > 0:
        gear_kosten = getItemsValueInGold(gear) * aantal_adventuring_investors
        aantal_paarden = aantal_adventuring_investors
        aantal_tenten = aantal_adventuring_investors
        kosten = getTotalRentalCost(aantal_paarden, aantal_tenten)
        eten_kosten = getJourneyFoodCostsInGold(aantal_adventuring_investors, aantal_paarden)
        total_price += gear_kosten + kosten + eten_kosten
    
    return round(total_price,2)

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    mensen = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    paarden = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)
    return math.floor(leftoverGold // (mensen + paarden))
    

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    mensen_kosten = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT * nightsInInn)
    paarden_kosten = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT * nightsInInn)
    return round(mensen_kosten + paarden_kosten,2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lijst = []
    for investor in investors:
        investor_cut = round(profitGold * investor['profitReturn'] / 100,2)
        if investor['profitReturn'] <= 10:
            lijst.append(investor_cut)
    return lijst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    total = 0.0
    for cut in investorsCuts:
        total += cut + fellowship
        try:
            total %= profitGold
        except ZeroDivisionError:
            total = 0.0
    return total

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()