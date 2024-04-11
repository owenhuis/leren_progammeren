def get_addition (number1, number2):
    return number1 + number2

def get_subtraction (number1, number2): 
    return number1 - number2

def get_multiplication (number1, number2):
    return number1 * number2

def get_division (number1, number2):
    return number1 / number2

def get_invoer():
    while True:
        try:
            number = int(input('voer een getal in: '))
            return number
        except ValueError:
            print('syntax error')