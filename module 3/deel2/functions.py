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
    amount = amount / 10
    amount = amount / 5
    return amount

def platinum2gold(amount:int) -> float:
    amount = amount * 25
    return amount

def getPersonCashInGold(personCash:dict) -> float:
    amount = 0
    for item in personCash:
        if item == 'copper':
            amount += copper2gold(personCash[item])
        if item == 'silver':
            amount += silver2gold(personCash[item])
        if item == 'gold':
            amount += personCash[item]
        if item == 'platinum':
            amount += platinum2gold(personCash[item])
    return amount

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    koste = 0
    koste += people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    koste += horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    koste = copper2gold(koste)
    return round(koste,2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    items = []
    for item in list:
        if key in item and item[key] == value:
            items.append(item)
    return items

def getAdventuringPeople(people:list) -> list:
    lijst = []
    for people in people:
        if people['adventuring'] == True:    
            lijst.append(people)
    return lijst

def getShareWithFriends(friends:list) -> list:
    lijst = []
    for vriend in friends:
        if vriend['shareWith'] == True:
            lijst.append(vriend)
    return lijst

def getAdventuringFriends(friends:list) -> list:
    items = []
    for item in friends:
        if item['adventuring'] == True and item['shareWith'] == True:
            items.append(item)
    return items

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    totaal_mensen = math.ceil(people/ 2)
    return totaal_mensen

def getNumberOfTentsNeeded(people:int) -> int:
    totaal_mensen = math.ceil(people/3)
    return totaal_mensen

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

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