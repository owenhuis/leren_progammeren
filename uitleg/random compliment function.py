import random
def get_random_compliment(naam: str) -> str:
    COMPLIMENTEN = ('je bent geweldig: ', 'Er is geen betere ', 'je bent de beste: ')
    random_compliment = random.choice(COMPLIMENTEN)
    return random_compliment + naam

print(get_random_compliment('owen'))